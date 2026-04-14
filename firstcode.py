# Dictionaries : Managing System Configuration
from xmlrpc import server


System_config = {"server_name" : "host - 1",
                 "uptime_days" : 45 ,
                 "is_active" : True ,
                 "authorised_users": ["admin","lead-dev","devops"]
                }

# Accessing specific data using keys
print(f"Connecting to:{System_config['server_name']}")

#Adding a new key-value pair to ditionary
System_config["max_connections"] = 100
print(f"Max connections allowed: {System_config['max_connections']}")

print(f"system status : {System_config}")

#File I/O : Reading and writing log files

#writing to a log file
with open("system_log.txt","w") as log_file:
    log_file.write("system started successfully\n")
    log_file.write("uptime : 45 days\n")

#reading from a log file
with open("system_log.txt","r") as log_file:
     log_content = log_file.read()
     print("----- Retrieved log data -----")
     print(log_content)

#OOP : creating a proffessional user structure
class system_user:
     def __init__(self,username,role):
          #'blueprint' for every user
           self.username = username
           self.role = role

     def display_info(self):
    # a mathod to display user info 
           print(f"User: {self.username} / role: {self.role}")

#creating actual objects from the blueprint
admin_user = system_user("admin","administrator")                
dev_user = system_user("devops","developer")

#using the objects 
admin_user.display_info()
dev_user.display_info()

#Blueprint for a proffessional server object
#getting a deep dive into OOP concepts like inheritance and encapsulation
class Server:
     def __init__ (self, name, ip_address):
 #Attributes : these are the "data" the objects holds
            self.name = name 
            self.ip_address = ip_address
            self.is_running = False  #default state of the server 

     #Methods : these are the actions the objects can perform
     def start_server(self):       
            self.is_running = True
            print(f"{self.name} has started.")

     def get_status(self):
            status = "running" if self.is_running else "stopped"
            print(f"{self.name } is currently {status}.")

#creating different objects from the same blueprint
web_server = Server("Web Server","192.168.1.10")       
db_server = Server("Database Server","192.168.1.20")

#interacting with the objects
web_server.start_server()
web_server.get_status()
db_server.get_status() #this will still be offline

#Advanced OOP : Inheritance and Encapsulation
class Cloudserver(Server):
     def __init__(self,name,ip_address, region):
           # i will bring 'super()' to get everythin from the parent class (server) and then add my own attribute
        super(). __init__(name,ip_address)
        self.region = region
        self._access_key = "SECURE_KEY_123" # Encapsulated (private) data

     def deploy_app(self, app_name):
         #this action is specialized and only cloud servers can do it
         print(f"Deploying {app_name} to {self.name} in {self.region} region...")

#creating a cloud server object
my_cloud_node = Cloudserver("Cloude_node_1","10.0.0.5","Ahmedabad")

#which has the Original Server actions plus its own unique features
my_cloud_node.start_server()

# And its new specialized actions !!!
my_cloud_node.deploy_app("Sakura_V1") 

#External Packages (supply line management) : using 'requests' to interact with APIs
import requests # basically recruiting the external tool

def check_internet_connectivity():
    """uses the requests package to varify the system's online status"""
    try:
        #here im trying to reach a standard professional endpoint
        response = requests.get("https://api.github.com", timeout=5)
        if response.status_code == 200:
            print("Connection is active : Access to GitHub API is active.")
        else:
            print("Internet connection is inactive.")
    except Exception as e:
        print(f"Connectivity error : System is offline or unreachable.{e}")

if __name__ == "__main__":
     check_internet_connectivity()