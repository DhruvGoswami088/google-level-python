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