from autogen import AssistantAgent
from configs.settings import AGENT_CONFIG, REPORTS_DIR
import os
import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

class ReporterAgent(AssistantAgent):
    def __init__(self):
        super().__init__(
            name="ReporterAgent",
            system_message="""You are the reporter agent responsible for:
1. Collecting all reconnaissance results
2. Organizing and structuring the data
3. Generating comprehensive reports
4. Highlighting important findings
5. Providing actionable insights""",
            llm_config=AGENT_CONFIG
        )
        
    def generate_report(self, url: str, results: dict) -> str:
        """
        Generate a comprehensive report from the reconnaissance results
        
        Args:
            url (str): The analyzed URL
            results (dict): Dictionary containing all analysis results
            
        Returns:
            str: Path to the generated report file
        """
        # Create report filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = os.path.join(REPORTS_DIR, f"report_{timestamp}.html")
        
        # Load template
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("report_template.html")
        
        # Generate report content
        report_content = template.render(
            url=url,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            results=results
        )
        
        # Save report
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
            
        return report_file
