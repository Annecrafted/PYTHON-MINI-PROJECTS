print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Okay, maybe next time! :(")
    quit()

print("Okay! Let's play :)")
score = 0

question = input("What does CPU stand for? ")
if question.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is Central Processing Unit.")
    

question = input("What does GPU stand for? ")
if question.lower() == "graphics processing unit":
    print("Correct!")   
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is Graphics Processing Unit.")

question = input("What does RAM stand for? ")
if question.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is Random Access Memory.")

question = input("What does PSU stand for? ")
if question.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The correct answer is Power Supply Unit.")

print("Congratulations! You have completed the quiz.")
print(f"Your final score is {score}/4.")
print(f"You got {score / 4 * 100}% correct!")


