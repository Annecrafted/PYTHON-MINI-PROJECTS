print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play ")

question = input("What does CPU stand for? ")
if question.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")
    print("The correct answer is Central Processing Unit.")
    quit()

question = input("What does GPU stand for? ")
if question.lower() == "graphics processing unit":
    print("Correct!")   
else:
    print("Incorrect!")
    print("The correct answer is Graphics Processing Unit.")
    quit()

question = input("What does RAM stand for? ")
if question.lower() == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")
    print("The correct answer is Random Access Memory.")
    quit()

question = input("What does PSU stand for? ")
if question.lower() == "power supply unit":
    print("Correct!")
else:
    print("Incorrect!")
    print("The correct answer is Power Supply Unit.")
    quit()

print("Congratulations! You have completed the quiz.")

