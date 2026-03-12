# Clawstrider

Clawstrider is a high-level orchestration SDK built for OpenClaw. It enables developers to define complex, multi-step agentic workflows where agents can pass state, execute tools via recursive reasoning, and collaborate on shared goals.

## Core Philosophical Pillars

1.  **Stateful Trajectories**: Every agent interaction is part of a traceable trajectory, allowing for rollbacks and state-dependent branching.
2.  **Tool-First Design**: Tools aren't just functions; they are first-class residents with schema validation and automatic retry logic.
3.  **OpenClaw Integration**: Native support for OpenClaw's prompt management and LLM abstraction layers.

## Installation

```bash
pip install clawstrider
```

## Quick Start

```python
from clawstrider import Swarm, Agent, Tool

# Define a simple tool
def get_weather(location: str):
    return f"The weather in {location} is sunny."

weather_tool = Tool(
    name="get_weather",
    func=get_weather,
    description="Fetches current weather for a city"
)

# Initialize an agent
researcher = Agent(
    name="Researcher",
    instructions="You find information using tools.",
    tools=[weather_tool]
)

# Orchestrate a workflow
swarm = Swarm(agents=[researcher])
result = swarm.run("What is the weather in Tokyo?")
print(result.final_output)
```

## Architecture

Clawstrider uses a **Plan-Act-Observe** loop:
- **Planner**: Determines the next logical step based on current history.
- **Executor**: Dispatches tool calls or agent transitions.
- **Monitor**: Validates outputs and manages the context window.

## Development

Check `CONTRIBUTING.md` for setup instructions.
