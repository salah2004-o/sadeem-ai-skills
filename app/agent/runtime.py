from __future__ import annotations

from app.agent.registry import SkillRegistry


class Agent:
    """Minimal routing agent for educational skill execution."""

    def __init__(self, registry: SkillRegistry) -> None:
        self.registry = registry

    def handle(self, user_input: str) -> str:
        command = user_input.strip()

        if not command:
            return ""

        if command.startswith("/"):
            parts = command.split(maxsplit=1)
            skill_name = parts[0][1:]
            skill_input = parts[1] if len(parts) > 1 else ""

            skill = self.registry.get(skill_name)
            return str(skill.execute(skill_input))

        return "Unknown command. Use /echo or /summarize."
