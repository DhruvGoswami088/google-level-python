while True:
 
    # I am adding .lower() at the end to handle EXIT,exit or ExIt etc...
 user_input = input("Enter RAM usage (or type 'exit' to quit): ").lower()
 
 if user_input == "exit":
   print("closing the system monitor ! , GoodBye ")
   break #to break the loop
 
 #if user inputs any actual number 
 if user_input.isdigit():
      ram = int(user_input)
      if ram > 7:
         print("close background apps !! , high ram usage alert !")
      else:
         print ("system stable!")

 else:
      print("invalid Input ! , please enter a valid number or type 'exit'!")
      print ("_"*15)