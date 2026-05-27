"""
Text preprocessing utilities for RADAR.

Shared between the training pipeline and the inference script so that
identical preprocessing is guaranteed at both stages.
"""

import re

_EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
_USER_RE = re.compile(r"@[A-Za-z0-9_-]+")
_PHONE_RE = re.compile(
    r"(\+?\d{1,3})?[\s\*\.\-]?\(?\d{1,4}\)?[\s\*\.\-]?\d{2,4}[\s\*\.\-]?\d{2,6}"
)


def preprocess(text: str) -> str:
    """
    Apply the same preprocessing pipeline used during training:

    1. Replace e-mail addresses with ``[EMAIL]``.
    2. Replace ``@username`` mentions with ``[USER]``.
    3. Replace phone numbers with ``[PHONE]``.
    4. Lowercase and strip leading / trailing whitespace.
    """
    text = _EMAIL_RE.sub("[EMAIL]", text)
    text = _USER_RE.sub("[USER]", text)
    text = _PHONE_RE.sub(" [PHONE]", text).replace("  [PHONE]", " [PHONE]")
    return text.lower().strip()
