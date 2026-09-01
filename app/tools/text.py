from __future__ import annotations


def clean_text(text: str) -> str:
    """Trim unnecessary whitespace while keeping the content readable."""
    return " ".join(text.strip().split())
