from clawstrider import Swarm, Agent, Tool

# 1. Define Tools
def search_docs(query: str):
    return f"Results for {query}: Clawstrider is easy to use."

docs_tool = Tool(
    name="search_docs",
    func=search_docs,
    description="Search through documentation"
)

# 2. Setup Specialized Agents
support = Agent(
    name="Support",
    instructions="You help customers with docs.",
    tools=[docs_tool]
)

billing = Agent(
    name="Billing",
    instructions="You handle payment queries.",
    tools=[]
)

# 3. Create Swarm
swarm = Swarm(agents=[support, billing])

# 4. Run complex query
if __name__ == "__main__":
    res = swarm.run("How do I install the SDK?")
    print(f"Response: {res.final_output}")
