from .base import LLM
from typing import Optional
import os
import openai
from ...exceptions import APIKeyNotFoundError, UnsupportedOpenAIModelError


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
        instruction: Optional[str] = None,
    ):
        self.api_token = api_token or os.getenv("OPENAI_API_KEY") or None

        if self.api_token is None:
            raise APIKeyNotFoundError("OpenAI API key is required")

        openai.api_key = self.api_token

        self.instruction = instruction

    def call(self, prompt: str) -> str:
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
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": f'{self.instruction}',
                    },
                    {"role": "user", "content": prompt},
                ],
            )

        else:
            raise UnsupportedOpenAIModelError("Unsupported model")

        return response
