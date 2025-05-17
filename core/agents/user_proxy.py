from autogen import UserProxyAgent
from core.tools.webtech_tool import analyze_technology

class ReconUserProxy(UserProxyAgent):
    def __init__(self):
        super().__init__(
            name="UserProxy",
            human_input_mode="NEVER",
            system_message="""You are a user proxy agent that:
1. Receives URLs from users
2. Validates and sanitizes input
3. Forwards requests to the Orchestrator
4. Returns final results to users""",
            function_map={
                "analyze_technology": analyze_technology
            }
        )
        
    def get_human_input(self, prompt: str) -> str:
        """Override to handle automated responses"""
        return "TERMINATE"  # Auto-terminate when human input is requested 