import unittest
from clawstrider import Swarm, Agent, Tool

class TestSwarmOrchestration(unittest.TestCase):
    def test_basic_flow(self):
        agent = Agent(name="Tester", instructions="Just reply.")
        swarm = Swarm(agents=[agent])
        result = swarm.run("Hello")
        self.assertTrue(result.final_output.startswith("Processed:"))

    def test_tool_schema(self):
        def my_tool(x: int, y: str):
            return f"{x}-{y}"
        tool = Tool("my_tool", my_tool, "A test tool")
        self.assertEqual(tool.name, "my_tool")
        self.assertIn("x", tool.schema["parameters"])

if __name__ == "__main__":
    unittest.main()
