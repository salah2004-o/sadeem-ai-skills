from __future__ import annotations

from app.skills import Skill


class SkillRegistry:
    """Simple registry for available skills."""

    def __init__(self) -> None:
        self._skills: dict[str, Skill] = {}

    def register(self, skill: Skill) -> None:
        self._skills[skill.name] = skill

    def get(self, name: str) -> Skill:
        try:
            return self._skills[name]
        except KeyError as exc:
            raise KeyError(f"Skill '{name}' is not registered.") from exc

    def all(self) -> list[Skill]:
        return list(self._skills.values())
