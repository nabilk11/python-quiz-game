# Computer Quiz Game
print("******** Welcome to the Computer Quiz ********")

playing = input("Would you like to play? ").lower()

if playing != "yes": # if true (anything but yes, will quit game
    print("Maybe Next Time!")
    quit() 

print("Then Let's Play!")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
else:
    print("Wrong :(")
answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit" or answer == "graphic processing unit":
    print("Correct!")
else:
    print("Wrong :(")
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
else:
    print("Wrong :(")
answer = input("What does PSU? ").lower()
if answer == "power supply unit":
    print("Correct!")
else:
    print("Wrong :(")