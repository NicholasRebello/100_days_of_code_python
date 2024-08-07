chest = r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
'''
print(chest)
print("\nWelcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

print("To the left you hear water running, to the right is a dense forest.")
choice = input("Left or right? ").lower()

if choice == "left":
    print("\nYou come across a river. There is a log someway downstream heading your way.")
    choice = input("Do you swim or wait? ").lower()
    if choice == "wait":
        print("\nYou wait for the log to get closer and then use it as a stepping stone to cross the river.")
        print("You see a mysterious building with 3 doors... blue, yellow, and red.")
        choice = input("Which door do you chose? ").lower()
        if choice == "red":
            print("You are burned by fire.")
        elif choice == "blue":
            print("You are eaten by beasts.")
        elif choice == "yellow":
            print("The treasure is there waiting for your claim!")
            print("You Win!")
            exit()
    else:
        print("You are attacked by trout.")
else:
    print("You fall into a hole.")

print("Gave Over.")
exit()
