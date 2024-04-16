import os
from dotenv import load_dotenv
from prompts.prompts import Prompts
from utils.common import normalize_json_str
from clients.openai import get_openai_client

load_dotenv()


class OpenaiUtils:
    def __init__(self) -> None:
        self.client = get_openai_client()
        self.prompts = Prompts()

    def get_prompt_result(self, type: str, html: str, meta: object):
        print(type)
        print(meta)
        content = None
        if type == "summary":
            content = self.prompts.get_website_summary(html)

        if content == None:
            return "content type not found"

        try:
            completion = self.client.chat.completions.create(
                model=os.environ.get("MODEL"),
                messages=[
                    {"role": "system", "content": content}
                    # {"role": "user", "content": prompts.user_message}
                ],
            )
            response = completion.choices[0].message.content
            print(completion.choices[0].message.content)
            return normalize_json_str(response)
        except Exception as e:
            print(e)
            raise
