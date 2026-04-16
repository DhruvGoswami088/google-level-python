# system tools - Advanced Function Architectures

def process_multi_data(command, *args, **kwargs):
    """
    a professional tool designed to handle unknown amounts of data.
    *args-captures extra values into a list.
    **kwargs-captures extra labeled data into a  dictionary.
    """
    print(f"Executing System Command: {command}")

    if args:
        print(f"Addtional Data Points: {args}")

    if kwargs:
        print("System Details :")
        for key , value in kwargs.items():
            print(f"- {key}:{value} ")

#test-1
process_multi_data("REBOOT")  #Simple

#test-2
process_multi_data("SYNC","Data_01","Data_02", priority="high", user="Dhruv") 
