command = ""
started = False

while True:
   command = input(">$ ").lower()
   if command == "start":
       if started :
           print("car is already started!")
       else:
            started = True
            print("Car started...") 
       print("car started....")
    
   elif command == "stop":
      if not started :
          print("Car is already stoped")
      else:
          started = False
          print("car has stoped ")   
   elif command == "help":
        print("""
use following commands
start - to start the car
stop - to stop the car
quit - to quit the game
""")
   elif command == "quit":
       print("Quiting the game")   
       break 
   else:
        print("sorry, Command not found!")        