from autogen import AssistantAgent
from configs.settings import AGENT_CONFIG

class WebTechAgent(AssistantAgent):
    def __init__(self):
        super().__init__(
            name="WebTechAgent",
            system_message="""You are a web technology expert agent. Your role is to:
1. Analyze websites to detect technologies being used
2. Process and interpret the results from web technology analysis
3. Provide detailed insights about the detected technologies
4. Format the results in a clear and structured way""",
            llm_config={
                **AGENT_CONFIG,
                "tools": [{
                    "type": "function",
                    "function": {
                        "name": "analyze_technology",
                        "description": "Analyze technologies used by a website using Wappalyzer",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "url": {
                                    "type": "string",
                                    "description": "The URL to analyze"
                                }
                            },
                            "required": ["url"]
                        }
                    }
                }]
            }
        )
