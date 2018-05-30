"""
This code for a game that requires you to guess a flag and get points
for each flag you guess correctly and each flag you guess wrong is minus a point
"""


#I need something that will add and subtract points 
#I will need some sort of indicator to see if the answer given is correct
#If correct will add points
#If not it will subtract a points
"""
I will also need some way to randomly distribut different answers so the
Questions are never the same
I will also need to make sure the right answer is in there somewhere
The hardest part will be to display a the image on the website
I will need to have a ton of flags downloaded so I can
Have lots of different questions and people can actually gain some knowledge
from my game
"""

import os
points = 0
print ("1 = Nigeria, 2 = Mozambique, 3 = South Africa, 4 = Djibuti")
os.startfile('Y:/ddccode2/finalproject/flag1.png')
print (" ")
answer = int(input("Which answer is correct?: "))
if answer == 2:
    print ("Nice job!")
    points = points + 1
else:
    print ("Sorry that's wrong.")
print ("Your current score is " + str(points))
check = input("Please close the image and press enter to proceed")
#This is repeated to get more questions
#Putting the code into a function would be problematic as the score wouldn't stay global
print ("1 = China, 2 = Japan, 3 = Thailand, 4 = Papa New Guiena")
os.startfile('Y:/ddccode2/finalproject/flag2.png')
print (" ")
answer = int(input("Which answer is correct?: "))
if answer == 3:
    print ("Nice job!")
    points = points + 1
else:
    print ("Sorry that's wrong.")
print ("Your current score is " + str(points))
check = input("Please close the image and Please close the image and press enter to proceed")
print ("1 = Finland, 2 = Sweden, 3 = Denmark, 4 = Germany")
os.startfile('Y:/ddccode2/finalproject/flag.png')
print (" ")
answer = int(input("Which answer is correct?: "))
if answer == 1:
    print ("Nice job!")
    points = points + 1
else:
    print ("Sorry that's wrong.")
print ("Your current score is " + str(points))
check = input("Please close the image and press enter to proceed")

print ("1 = Mongolia, 2 = Grenada, 3 = Loas, 4 = Saint Lucia")
os.startfile('Y:/ddccode2/finalproject/flag3.png')
print (" ")
answer = int(input("Which answer is correct?: "))
if answer == 1:
    print ("Nice job!")
    points = points + 1
else:
    print ("Sorry that's wrong.")
print ("Your current score is " + str(points))
check = input("Please close the image and press enter to proceed")


print ("1 = Honduras, 2 = Niger, 3 = El Salvador, 4 = Tuvalu")
os.startfile('Y:/ddccode2/finalproject/flag4.png')
print (" ")
answer = int(input("Which answer is correct?: "))
if answer == 4:
    print ("Nice job!")
    points = points + 1
else:
    print ("Sorry that's wrong.")
print ("Your current score is " + str(points))
check = input("Please close the image and press enter to proceed")


if points >= 3:
    bonusQuestion = input("Nice job!! Do you want to do a bonus question? Answer yes or no: ")
    if bonusQuestion == "yes":
        print ("1 = Republic of Moldova, 2 = Cambodia, 3 = Liechtenstein, 4 = Marshall Islands")
        os.startfile('Y:/ddccode2/finalproject/flag5.png')
        print (" ")
        answer = int(input("Which answer is correct?: "))
        if answer == 1:
            print ("Nice job!")
            points = points + 1
        else:
            print ("Sorry that's wrong.")
    else:
        print ("Nice job anyways.")
if answer == 4:
    print ("Nice job!")
    points = points + 1
else:
    print ("Nice try you'll do better next time")
