# main.py - The entry point of your professional system
import utility #importing my own custom module !
system_info = {
     "server_id" : "Alpha-9",
     "region": "mumbai",
     "load": "low"
}

# Now Using the tools from my Utility module
print(utility.foramt_system_report(system_info))
print(f"Annual reliability : {utility.calculate_uptime_percentage(320)}")