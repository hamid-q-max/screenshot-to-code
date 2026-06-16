# Useful for debugging purposes when you don't want to waste GPT4-Vision credits
# Setting to True will stream a mock response instead of calling the OpenAI API
# TODO: Should only be set to true when value is 'True', not any arbitrary truthy value
import os

NUM_VARIANTS = 2

def _env_bool(var_name: str, default: bool = False) -> bool:
    """Parse a boolean environment variable.

    Treats common truthy strings ("1", "true", "yes", "on") as True and common
    falsy strings ("0", "false", "no", "off") as False. If the variable is
    unset/empty, returns the provided default.
    """

    raw = os.environ.get(var_name)
    if raw is None:
        return default

    value = raw.strip().lower()
    if value in {"1", "true", "yes", "y", "on"}:
        return True
    if value in {"0", "false", "no", "n", "off"}:
        return False

    return default


# LLM-related
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", None)
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", None)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", None)
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL", None)

# Image generation (optional)
REPLICATE_API_KEY = os.environ.get("REPLICATE_API_KEY", None)

# Debugging-related
SHOULD_MOCK_AI_RESPONSE = _env_bool("MOCK", False)
IS_DEBUG_ENABLED = _env_bool("IS_DEBUG_ENABLED", False)
DEBUG_DIR = os.environ.get("DEBUG_DIR", "")

# Set to True when running in production (on the hosted version)
# Used as a feature flag to enable or disable certain features
IS_PROD = _env_bool("IS_PROD", False)


def get_debug_log_path(filename: str) -> str:
    """Return the full path for a debug log file within the configured debug dir."""

    return DEBUG_DIR + "/" + filename


def is_production_mode() -> bool:
    """Return True when the application is running in production mode."""

    return bool(IS_PROD)


def is_admin(user) -> bool:
    """Return whether the given user should be treated as an admin.

    Note: this is currently a placeholder implementation.
    """

    return True
