from __future__ import annotations

from app.skills import Skill


class EchoSkill(Skill):
    """Return the input text exactly as received."""

    name = "echo"
    description = "Return the given text exactly."

    def execute(self, text: str) -> str:
        return text
