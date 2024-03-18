import os
import openai

from dotenv import load_dotenv

load_dotenv()


class ChatGPT:

    temperature = 0
    max_tokens = 1000
    top_p = 1
    frequency_penalty = 0
    presence_penalty = 0.6
    model = "gpt-3.5-turbo"

    def __init__(self, model: str):
        api_key = os.environ.get("OPENAI_API_KEY")
        if api_key is None:
            raise Exception(
                "Please set OPENAI_API_KEY environment variable."
                "You can obtain API key from https://platform.openai.com/account/api-keys"
            )
        openai.api_key = api_key
        self.model = model

    @property
    def _default_params(self):
        return {
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "top_p": self.top_p,
            "frequency_penalty": self.frequency_penalty,
            "presence_penalty": self.presence_penalty,
            "model": self.model,
        }

    def chat(self, prompt):
        client = openai.OpenAI()

        params = {
            **self._default_params,
            "messages": [
                {
                    "role": "system",
                    "content": prompt,
                }
            ],
        }
        response = client.chat.completions.create(**params)
        return response.choices[0].message.content
