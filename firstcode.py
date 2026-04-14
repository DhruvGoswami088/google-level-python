# Dictionaries : Managing System Configuration
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