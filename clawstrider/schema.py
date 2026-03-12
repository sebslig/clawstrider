from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class SwarmContext:
    history: List[Dict[str, Any]] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def add_history(self, agent_name: str, response: Any):
        self.history.append({
            "agent": agent_name,
            "content": response.content,
            "complete": response.is_complete
        })

@dataclass
class AgentResponse:
    content: str
    next_agent: Optional[str] = None
    is_complete: bool = False
    tool_calls: List[Dict[str, Any]] = field(default_factory=list)

@dataclass
class SwarmResult:
    final_output: str
    history: List[Dict[str, Any]]
    metadata: Dict[str, Any]
