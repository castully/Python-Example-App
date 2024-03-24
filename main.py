# main.py
# Chris Tully 2024

# Import
from area import calc_area

# Print the Main Menu.
def dispMenu():
    print("\n==== WELCOME TO the App ===")
    print("1 - Calculate Area of a Rectangle")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - Quit")


######  MAIN PROGRAM #######
    
# repeat this until user enters a "5"
response = 0 #initialization & first time through the while loop
while response != "5":
    
    dispMenu()
    response = input("\nPlease select menu choice: ")
    
    if response == "1": # Calculate Area of a Rectangle
        calc_area()
        
    elif response == "5": # Quit
        print("=== Goodbye! ===")

    else:
        print("Invalid response, please re-enter")