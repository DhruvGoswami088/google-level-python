# perception.py - Refined Perception Module
import requests

def get_web_status():
    """Fetches real-time system data from a production-grade API."""
    # Using GitHub's Public API for system verification
    url = "https://api.github.com/zen" 
    
    try:
        response = requests.get(url, timeout=5)
        # 200 is the industry 'OK' code
        if response.status_code == 200:
            return f"Perception Active: {response.text}"
        else:
            return f"Service Alert: Received status {response.status_code}"
            
    except requests.exceptions.SSLError:
        return "Security Alert: Target server has an invalid SSL certificate."
    except Exception as e:
        return f"Perception Error: {e}"

if __name__ == "__main__":
    print(get_web_status())