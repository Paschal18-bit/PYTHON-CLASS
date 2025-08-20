"""
This program takes a user's name and destination choice
(starting point: Aptech).  
The user can choose either **Abakpa** or **Emene** as their destination.  
The program then gives directions from Aptech to the chosen location.
"""

# Get user details
name = input("Enter your name: ")
destination = input("Where do you want to go (Abakpa/Emene)? ").strip().lower()

print(f"\nHello {name}!")

# Check the destination and give directions
if destination == "abakpa":
    print("From Aptech, take a bus heading towards Abakpa, "
          "stop at Abakpa junction, then continue straight to your destination.")

elif destination == "emene":
    print("From Aptech, take a bus going towards Emene, "
          "stop at Emene junction, and follow the main road to your destination.")

else:
    print("Sorry, I can only give directions to Abakpa or Emene.")
