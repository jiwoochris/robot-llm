from .base import LLM
from typing import Optional
import os
from dotenv import load_dotenv
import openai
from ...exceptions import APIKeyNotFoundError, UnsupportedOpenAIModelError


load_dotenv()


class OpenAI(LLM):
    """OpenAI LLM"""

    _supported_chat_models = [
        "gpt-4",
        "gpt-4-0613",
        "gpt-4-32k",
        "gpt-4-32k-0613",
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-16k",
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
    ]

    model: str = "gpt-3.5-turbo"

    def __init__(
        self,
        api_token: Optional[str] = None,
    ):
        self.api_token = api_token or os.getenv("OPENAI_API_KEY") or None

        if self.api_token is None:
            raise APIKeyNotFoundError("OpenAI API key is required")

        openai.api_key = self.api_token

    def call(self, instruction: str, prompt: str) -> str:
        """
        Call the OpenAI LLM.

        Args:
            instruction (prompt): Instruction to pass

        Raises:
            UnsupportedOpenAIModelError: Unsupported model

        Returns:
            str: Response
        """

        if self.model in self._supported_chat_models:
            completion = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": f"{instruction}",
                    },
                    {"role": "user", "content": prompt},
                ],
            )

            response = completion.choices[0].message.content.strip()

        else:
            raise UnsupportedOpenAIModelError("Unsupported model")

        return response
