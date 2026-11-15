"""AIGROW model-provider plugin for Hermes Agent."""

from providers import register_provider
from providers.base import ProviderProfile

# The ids match AIGROW's models.dev record (provider id "aigrow"). The profile
# name is the same id, so Hermes takes context windows and capabilities from
# that record instead of a second copy kept here.
AIGROW_MODELS = (
    "claude-opus-5.5",
    "claude-sonnet-5.5",
    "claude-fable-5.2",
    "claude-fable-5.1",
    "gpt-6.1-sol",
    "gpt-6.1-terra",
    "gpt-6-astra",
    "gemini-4-argon",
    "grok-4.7",
)

aigrow = ProviderProfile(
    name="aigrow",
    display_name="AIGROW",
    description="AIGROW: prepaid credit for Claude, GPT, Gemini and Grok on one OpenAI-compatible API",
    signup_url="https://aigrow.gg/ai-api",
    env_vars=("AIGROW_API_KEY",),
    base_url="https://aigrow.gg/v1",
    models_url="https://aigrow.gg/v1/models",
    auth_type="api_key",
    default_aux_model="gpt-6.1-terra",
    fallback_models=AIGROW_MODELS,
)

register_provider(aigrow)
