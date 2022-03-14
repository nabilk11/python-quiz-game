# Computer Quiz Game

# WELCOME + START INPUT
print("******** Welcome to the Computer Quiz ********")

playing = input("Would you like to play? ").lower()

if playing != "yes": # if true (anything but yes, will quit game
    print("Maybe Next Time!")
    quit() 

print("Then Let's Play!")
score = 0

# QUESTIONS
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong :(")
answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit" or answer == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong :(")
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong :(")
answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Wrong :(")

# BONUS ROUND
print("Here Comes the Bonus Question! 2pts if You're Correct, -1pt if You're Wrong!")
answer = input("What does SSD stand for? ").lower()
if answer == "solid state drive":
    print("Correct! 2pts added to your score!")
    score += 2
else:
    print("Wrong, -1pt from your score :(")
    score -= 1

# SCORE RESULTS
print("You're total score was " + str(score) + "pts!")

if score == 6:
    print("A Perfect Score of " + str(score/4 * 100) + "%!")
else:
    print("That's " + str(score/4 * 100) + "%!")