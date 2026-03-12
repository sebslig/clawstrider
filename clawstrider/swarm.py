import logging
from typing import List, Optional, Dict, Any
from .agent import Agent
from .schema import SwarmResult, SwarmContext

logger = logging.getLogger(__name__)

class Swarm:
    """Orchestrates a collection of agents to complete a task."""
    
    def __init__(self, agents: List[Agent], max_turns: int = 10):
        self.agents = {a.name: a for a in agents}
        self.max_turns = max_turns
        self.context = SwarmContext()

    def run(self, prompt: str, initial_agent: Optional[str] = None) -> SwarmResult:
        """Execute the workflow starting with a specific agent."""
        current_agent_name = initial_agent or list(self.agents.keys())[0]
        current_input = prompt
        
        for turn in range(self.max_turns):
            agent = self.agents.get(current_agent_name)
            if not agent:
                raise ValueError(f"Agent {current_agent_name} not found")
            
            logger.info(f"Turn {turn}: {current_agent_name} processing...")
            response = agent.execute(current_input, self.context)
            
            self.context.add_history(current_agent_name, response)
            
            if response.is_complete:
                return SwarmResult(
                    final_output=response.content,
                    history=self.context.history,
                    metadata={"turns": turn + 1}
                )
            
            if response.next_agent:
                current_agent_name = response.next_agent
                current_input = response.content
            
        return SwarmResult(
            final_output="Max turns reached without completion.",
            history=self.context.history,
            metadata={"error": "timeout"}
        )
