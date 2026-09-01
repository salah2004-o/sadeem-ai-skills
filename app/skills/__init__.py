from __future__ import annotations

from abc import ABC, abstractmethod


class Skill(ABC):
    """Base class for all skills."""

    name: str = ""
    description: str = ""

    @abstractmethod
    def execute(self, text: str) -> str:
        """Execute the skill with the provided text."""
        raise NotImplementedError
