from autogen import AssistantAgent
from configs.settings import AGENT_CONFIG

class OrchestratorAgent(AssistantAgent):
    def __init__(self):
        super().__init__(
            name="OrchestratorAgent",
            system_message="""You are the orchestrator agent responsible for:
1. Receiving and validating input URLs from users
2. Coordinating tasks between specialized agents (WebTech, etc.)
3. Collecting and aggregating results from all agents
4. Ensuring the reconnaissance process runs smoothly
5. Handling errors and providing status updates""",
            llm_config=AGENT_CONFIG
        )
        
    def validate_url(self, url: str) -> bool:
        """
        Validate if the input URL is properly formatted
        
        Args:
            url (str): URL to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        import re
        url_pattern = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return url_pattern.match(url) is not None
