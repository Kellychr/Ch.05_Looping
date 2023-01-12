'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random

print("you stole a camel \n  and you are being chased by natives")
print( )
print( )
print( )

thirst=0
tiredness=0
distance = 0
pirates=-20
gas=20
drinks=5
piratedis = random.randint(7,14)
full= random.randint(10,20)
tired= random.randint(1,3)
moderate= random.randint(5,12)
done = False
while not done:
    print("---------------------------------------------")
    print("A. Drink From your canteen")
    print("B. ahead moderate speed")
    print("C. ahead full speed")
    print("D. stop for the night")
    print("E. status check")
    print("Q. Quit")
    answer = str(input("what would you like to do? "))
    print( )
    print("--------------------------------------------------")




#     num=random.randint(1,21)
#
# if num==1:
#     thirst=0
#     drinks=5
#     tiredness=0
#     print("you found a oasis your water is refilled and your tiredness is back to 0")






    if answer.lower()=="d":
        # num=random.randint(1,3)
        #
        # if num==1:
        #     print("You stopped at a planet and and refueled for the night")
        # elif num==2:
        #     print("You went to a small planet and stole gas")
        # else:
        #     print("You managed to find a small abandoned base on a exoplanet with fuel")

        print("You rest for the night" )
        tiredness=0
        pirates+=piratedis
        gas+=tired
        print()
        print("-----------------------------")

    if answer.lower()=="a":
        print("You take a drink.")
        drinks-=1
        thirst=0

        print(drinks)
        print("-----------------------------")


    if answer.lower()=="b":
        print("You move ahead at a steady pace")
        moderate+=distance
        tired+=tiredness
        thirst+=1
        print(distance)
        piratedis+=pirates
        print(tiredness)
        print("-----------------------------")


    if answer.lower()=="c":
        print("You power through to escape the natives but you get very tired")
        full+=distance
        print(distance)
        thirst-=1
        tired+=tiredness
        print(tiredness)


    if answer.lower()=="e":
        print("You have traveled",distance,"miles")
        print("the natives are",piratedis,"miles away")
        print("you have",drinks,"drinks left")

    if distance >= 100:
        print("you win you out ran the natives")
        break

    if tiredness == 4:
        print("the camel is getting tired")

    if tiredness == 6:
        print("camel died")
        break



