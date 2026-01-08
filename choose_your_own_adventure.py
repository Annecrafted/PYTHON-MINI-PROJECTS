name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way do you want to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator. Game over.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    
    if answer == "back":
        print("You decided to head back and got lost. Game over.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
        if answer == "yes":
            print("You talked to the stranger and they gave you gold. You win!")
        elif answer == "no":
            print("You ignored the stranger and they felt offended. Game over.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thanks for playing", name)
