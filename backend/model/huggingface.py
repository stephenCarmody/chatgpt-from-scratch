import os
from typing import Dict, List, Optional

import requests

from settings import settings


class HuggingFaceInference:
    def __init__(
        self,
        api_token: Optional[str] = None,
        model_name: str = "meta-llama/Llama-2-7b-chat-hf",
    ):
        """Initialize the Hugging Face inference client."""

        self.api_token = api_token or settings.huggingface_api_key
        if not self.api_token:
            raise ValueError(
                "Please provide a Hugging Face API token either directly or via HF_API_TOKEN environment variable"
            )

        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}

    def generate(
        self, prompt: str, max_length: int = 1000, temperature: float = 0.7
    ) -> str:
        """Generate a response from the model."""
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_length": max_length,
                "temperature": temperature,
                "return_full_text": False,
            },
        }

        response = requests.post(self.api_url, headers=self.headers, json=payload)

        if response.status_code != 200:
            raise Exception(
                f"API request failed with status code {response.status_code}: {response.text}"
            )

        return response.json()[0]["generated_text"]

    def chat(self, messages: List[Dict[str, str]]) -> str:
        """Have a conversation with the model.

        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
                     role should be either 'user' or 'assistant'

        Returns:
            Model's response
        """
        # Format messages into the model's chat format
        prompt = ""
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "user":
                prompt += f"[INST] {content} [/INST]\n"
            elif role == "assistant":
                prompt += f"{content}\n"

        return self.generate(prompt)


def main():
    """Example usage of the HuggingFaceInference class."""

    model = HuggingFaceInference()
    messages = [{"role": "user", "content": "What is the capital of France?"}]

    try:
        response = model.chat(messages)
        print("Model:", response)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
