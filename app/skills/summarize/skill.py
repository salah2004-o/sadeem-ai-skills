from __future__ import annotations

import os

from dotenv import load_dotenv
from google import genai

from app.skills import Skill
from app.tools.text import clean_text

load_dotenv()


class SummarizeSkill(Skill):
    """Summarize input text using the Gemini API."""

    name = "summarize"
    description = "Summarize the provided text using Gemini."

    def execute(self, text: str) -> str:
        cleaned_text = clean_text(text)

        if not cleaned_text:
            return "No text provided for summarization."

        api_key = os.getenv("GEMINI_API_KEY")
        model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

        if not api_key:
            return "GEMINI_API_KEY is not set. Add it to your .env file."

        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=model,
            contents=(
                "Summarize the following text in a clear and concise way. "
                f"Return only the summary:\n\n{cleaned_text}"
            ),
        )

        return getattr(response, "text", str(response))
