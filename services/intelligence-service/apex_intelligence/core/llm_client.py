"""Pluggable LLM client.

This is a minimal implementation that echoes the prompt back. To integrate
with real providers, implement API calls here and use environment variables
to configure keys and endpoints.
"""


class LLMClient:
    """Client used to obtain completions from an LLM provider."""

    async def complete(self, prompt: str, max_tokens: int = 256) -> str:
        """Return a completion for the prompt.

        Parameters
        ----------
        prompt: str
            The input text
        max_tokens: int
            The maximum number of tokens to generate (unused in this stub)

        Returns
        -------
        str
            A dummy completion
        """
        # This stub just returns the prompt with a canned suffix. Replace
        # this method with calls to OpenAI, Azure OpenAI, Anthropic, etc.
        return f"[LLM]: You said '{prompt}'. This is a stub response."
