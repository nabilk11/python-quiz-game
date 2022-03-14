# Computer Quiz Game
print("******** Welcome to the Computer Quiz ********")

playing = input("Would you like to play? ").title()

if playing != "Yes" and playing != "YES": # if true (anything but yes, will quit game
    quit() 

print("Let's Play!")

answer = input("What does CPU stand for? ").title()
if answer == "Central Processing Unit" and answer != "CENTRAL PROCESSING UNIT":
    print("Correct!")
else:
    print("Wrong :(")
answer = input("What does GPU stand for? ").title()
if answer == "Graphics Processing Unit" and answer != "GRAPHICS PROCESSING UNIT":
    print("Correct!")
else:
    print("Wrong :(")
answer = input("What does RAM stand for? ").title()
if answer == "Random Access Memory" and answer != "RANDOM ACCESS MEMORY":
    print("Correct!")
else:
    print("Wrong :(")
answer = input("What does PSU? ").title()
if answer == "Power Supply Unit" and answer != "POWER SUPPLY UNIT":
    print("Correct!")
else:
    print("Wrong :(")