import os
from langchain.embeddings.openai import OpenAIEmbeddings
import openai
from prompts import Prompts
from constants.constants import *
from prompts import Prompts

os.environ["OPENAI_API_TYPE"] = ""
os.environ["OPENAI_API_BASE"] = ""
os.environ["OPENAI_API_KEY"] = ""
os.environ["OPENAI_API_VERSION"] = ""


class LLMUtils:
    def __init__(self) -> None:
        self.embeddings = OpenAIEmbeddings(
            deployment=DEPLOYMENT,
            model=MODEL,
            openai_api_base=OPENAI_API_BASE,
            openai_api_type=OPENAI_API_TYPE,
            chunk_size=1
        )
        self.prompts = Prompts()

    def chat_completion(self, context, query):
        prompt = self.prompts.create_prompt(context, query)

        response = openai.ChatCompletion.create(
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant'},
                {'role': 'user', 'content': prompt},
            ],
            engine="LawBook",
            temperature=0,
        )

        bot_response = response.get("choices")[0].get('message').get('content')
        cost_per_query = float(response.get("usage").get("total_tokens")) / 1000 * 0.002

        return bot_response, cost_per_query
