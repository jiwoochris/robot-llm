"""Robot-LLM's custom exceptions.

This module contains the implementation of Custom Exceptions.

"""


class APIKeyNotFoundError(Exception):

    """

    Args:
        Exception (Exception): APIKeyNotFoundError
    """


class UnsupportedOpenAIModelError(Exception):

    """

    Args:
        Exception (Exception): UnsupportedOpenAIModelError
    """


class MethodNotImplementedError(Exception):

    """

    Args:
        Exception (Exception): MethodNotImplementedError
    """


class NeitherChatNorRequest(Exception):

    """

    Args:
        Exception (Exception): NeitherChatNorRequest
    """
