from typing import Dict, Any

def validate_tool_args(schema: Dict[str, Any], args: Dict[str, Any]):
    """Basic validation for tool arguments against schema."""
    expected = schema.get("parameters", {})
    for key, info in expected.items():
        if info.get("required") and key not in args:
            raise ValueError(f"Missing required argument: {key}")
    return True
