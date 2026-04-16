# Decorators - the power-up system !

def system_logger(func):
    def wrapper(*args, **kwargs):
        print(f"[log]: Running activity: {func.__name__}...")
        result = func(*args, **kwargs)  #execute the original function
        print(f"[log]: Activity Completed.")
        return result
    return wrapper

@system_logger
def update_database(data):
    """the actual tool we want to power up"""
    print(f"Working: Syncing '{data}' to the server...")

#testing
update_database("User_Profile_Data")