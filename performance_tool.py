import time 
def speed_test(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  #start timer
        result = func(*args, **kwargs) 
        end_time = time.time() #end timer
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@speed_test
def simulate_heavy_loading():
    print("loading system assets...")
    time.sleep(1.5) #forcing a 1.5 sec. delay

simulate_heavy_loading()