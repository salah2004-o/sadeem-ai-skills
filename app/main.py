from __future__ import annotations

from app.agent.registry import SkillRegistry
from app.agent.runtime import Agent
from app.skills.echo.skill import EchoSkill
from app.skills.summarize.skill import SummarizeSkill


def build_registry() -> SkillRegistry:
    registry = SkillRegistry()
    registry.register(EchoSkill())
    registry.register(SummarizeSkill())
    return registry


def main() -> None:
    registry = build_registry()
    agent = Agent(registry)

    print("Sadeem AI Agent")
    print()

    while True:
        user_input = input("YOU: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if user_input.lower() == "skills":
            print("Available skills:")
            for skill in registry.all():
                print(f"- {skill.name}")
            continue

        result = agent.handle(user_input)
        print(f"AGENT: {result}")


if __name__ == "__main__":
    main()
