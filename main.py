print('''
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("To reach your destination you have a crossroad. Now this path will either bring you chose to the treasure or to your doom!!")
path = input("Which path will you choose? Right or Left? ").lower()
if path == "left" :
          print("You\'ve reached the sea of silence")
          lake = input("You've reached the sea of silence. Will you swim or wait for the boat? Swim or Wait? ").lower()
          if lake == "wait":
                    print("Reached the demon lord castle")
                    door = input("You have reached treasure chamber. Choose between 3 doors? Red or Blue or Yellow? ").lower()
                    if door == "red":
                              print("Game Over. You have fallen into fiery pit.")
                    elif door == "blue":
                              print("Game Over. You have fallen into ruler of the sea of silence chamber.")
                    elif door == "yellow":
                              print("Congratulation. You have reached the treasure.") 
                    else:
                              print("Game Over. You\'ve choose a door that don\'t exist.")
          else:
                    print("Game Over. You faced the wrath of the lord of silent sea.")
else:
          print("Game Over. You have fallen into the abyss.")


          
          
          

                    
                    
                    