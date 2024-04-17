import json

# 1. import boto3
import boto3

# 2 create client connection with bedrock
client_bedrock_knowledgebase = boto3.client("bedrock-agent-runtime")
modelArn = "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-instant-v1"
knowledgeBaseId = "KAC9NBMMM7"
promptTemplate =  "You're the friendly AI chatbot for Home24, an e-commerce site specializing in furniture. Use your knowledge base to help customers with their inquiries, always maintaining a warm and approachable tone."

def extract_s3_locations(json_data):
    try:
        unique_urls = set()
        citations = json_data.get("citations", [])
        for citation in citations:
            retrieved_references = citation.get("retrievedReferences", [])
            for reference in retrieved_references:
                location = reference.get("location", {})
                if location.get("type") == "S3":
                    url = location.get("s3Location", {}).get("uri")
                    unique_urls.add(url)
        return list(unique_urls)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []


# https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html


def lambda_handler(event, context):
    # 3 Store the user prompt
    print(event["prompt"])
    print(event["sessionId"])
    user_prompt = event["prompt"]
    session_id = event["sessionId"]

    if session_id != "None":
        client_knowledgebase = client_bedrock_knowledgebase.retrieve_and_generate(
            input={"text": user_prompt},
            retrieveAndGenerateConfiguration={
                "type": "KNOWLEDGE_BASE",
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": knowledgeBaseId,
                    "modelArn": modelArn,
                },
            },
        )
    else:
        client_knowledgebase = client_bedrock_knowledgebase.retrieve_and_generate(
            input={"text": user_prompt},
            retrieveAndGenerateConfiguration={
                "generationConfiguration": { 
                    "promptTemplate": { 
                       "textPromptTemplate":promptTemplate
                    }
                 },
                "type": "KNOWLEDGE_BASE",
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": knowledgeBaseId,
                    "modelArn": modelArn,
                },
            },
            sessionId=session_id,
        )

    print(client_knowledgebase)

    s3_locations = extract_s3_locations(client_knowledgebase)
    response_kbase_final = client_knowledgebase["output"]["text"]
    return {"statusCode": 200, "body": response_kbase_final, "locations": s3_locations, "session_id": client_knowledgebase["sessionId"]}
