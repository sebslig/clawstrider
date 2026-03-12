from typing import List, Callable, Any, Dict
import inspect

class Tool:
    """Wraps a python function for agent usage."""
    
    def __init__(self, name: str, func: Callable, description: str):
        self.name = name
        self.func = func
        self.description = description
        self.schema = self._generate_schema()

    def _generate_schema(self) -> Dict[str, Any]:
        sig = inspect.signature(self.func)
        params = {}
        for name, param in sig.parameters.items():
            params[name] = {
                "type": str(param.annotation),
                "required": param.default is inspect.Parameter.empty
            }
        return {
            "name": self.name,
            "description": self.description,
            "parameters": params
        }

    def __call__(self, **kwargs) -> Any:
        return self.func(**kwargs)
