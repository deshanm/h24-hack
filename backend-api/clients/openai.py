import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

def get_openai_client() -> AzureOpenAI:
    return AzureOpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
            api_version=os.environ.get("API_VERSION"),
            azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
        )