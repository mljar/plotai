import os
import boto3
from botocore.exceptions import ClientError

from dotenv import load_dotenv

load_dotenv()



class Bedrock:


    def __init__(self, model: str, region_name: str = "us-east-1"):
        profile_name = os.environ.get("AWS_PROFILE")
        if profile_name is None:
            raise Exception(
                "Please set AWS_PROFILE environment variable."
                "You can obtain API key from https://console.aws.amazon.com/iam/home#/security_credentials"
            )
        self.region_name = region_name
        self.session = boto3.Session(profile_name=profile_name)
        self.model = model
        self.client = self.session.client("bedrock-runtime", region_name=self.region_name)


    def chat(self, prompt):
        conversation = [
            {
                "role": "user",
                "content": [{"text": prompt}],
            }
        ]
        try:
            response = self.client.converse(
                modelId=self.model,
                messages=conversation,
                inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
            )
            response_text = response["output"]["message"]["content"][0]["text"]
            return response_text
        except (ClientError, Exception) as e:
            return f"ERROR: Can't invoke '{self.model}'. Reason: {e}"


# br = Bedrock("anthropic.claude-3-5-sonnet-20240620-v1:0")

# print(br.chat("Tell me a joke"))
