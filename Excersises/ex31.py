print("You enter a dark room with two doors. Do you go through doors #1 or #2?.")

door=input(">")

if door=="1":
    print("There is a gaint bear here eating a cheese cake.What do you do?")
    print("1. Take the cake")
    print("2. scream at the bear.")

    bear=input(">")

    if bear=="1":
        print("The bear eats your face off .  Good Job!")

    elif bear==2:
        print("The bear eats your leg off. Good job!")

    else:
        print("Well, doing %s is probably better. Bear runs away"%bear)

elif door=="2":
    print("There is a loin")

    print("1. I watch it.")
    print("2. I swim.")
    print("3. I run!")

    option=input('>')

    if option=="1" or option=="2":
        print("Good Job!, You win the game.")

    else:
        print("Sad , u lost the game")
