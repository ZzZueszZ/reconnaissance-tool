from Wappalyzer import Wappalyzer, WebPage
import requests
import json
import os
from configs.settings import RAW_DATA_DIR

def analyze_technology(url: str) -> dict:
    """
    Analyze the technologies used by a website using Wappalyzer
    
    Args:
        url (str): The URL to analyze
        
    Returns:
        dict: Dictionary containing detected technologies
    """
    try:
        # Initialize Wappalyzer
        wappalyzer = Wappalyzer.latest()
        
        # Fetch webpage
        webpage = WebPage.new_from_url(url)
        
        # Analyze technologies
        analysis = wappalyzer.analyze_with_versions_and_categories(webpage)
        
        # Save raw data
        output_file = os.path.join(RAW_DATA_DIR, f"{url.replace('://', '_').replace('/', '_')}_tech.json")
        with open(output_file, 'w') as f:
            json.dump(analysis, f, indent=2)
            
        return {
            "status": "success",
            "technologies": analysis,
            "raw_data_file": output_file
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        } 