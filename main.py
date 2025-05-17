from autogen import GroupChat, GroupChatManager
from core.agents.user_proxy import ReconUserProxy
from core.agents.orchestrator import OrchestratorAgent
from core.agents.webtech_agent import WebTechAgent
from core.agents.reporter import ReporterAgent
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('recon.log')
    ]
)

logger = logging.getLogger(__name__)

def main(url: str):
    """
    Main function to run the reconnaissance flow
    
    Args:
        url (str): Target URL to analyze
    """
    try:
        # Initialize agents
        user_proxy = ReconUserProxy()
        orchestrator = OrchestratorAgent()
        webtech_agent = WebTechAgent()
        reporter = ReporterAgent()
        
        # Create group chat
        groupchat = GroupChat(
            agents=[user_proxy, orchestrator, webtech_agent, reporter],
            messages=[],
            max_round=10
        )
        
        manager = GroupChatManager(groupchat=groupchat)
        
        # Start the reconnaissance flow
        logger.info(f"Starting reconnaissance for URL: {url}")
        
        # Initial message to start the flow
        initial_message = f"""
        Please analyze the following URL: {url}
        
        Steps:
        1. Orchestrator: Validate URL and coordinate analysis
        2. WebTechAgent: Analyze web technologies
        3. Reporter: Generate comprehensive report
        """
        
        # Start the chat
        result = user_proxy.initiate_chat(
            manager,
            message=initial_message
        )
        
        logger.info("Reconnaissance completed successfully")
        return result
        
    except Exception as e:
        logger.error(f"Error during reconnaissance: {str(e)}")
        raise

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        sys.exit(1)
        
    url = sys.argv[1]
    main(url)
