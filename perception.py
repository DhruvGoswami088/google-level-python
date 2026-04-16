import requests
def get_web_status():
    """Fetches real-time data to verify internet perception"""
    
    try:
        #Fetching a random professional quote a data test
        response = requests.get("https://api.quotable.io/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f"Perception Active :{data['content']}" 
        return "Warning : Web service unreachable."
    except Exception as e:
        return f"perception error: {e}"
    
    if __name__ == "__main__":
        print(get_web_status())
