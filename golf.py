#
# Python:   3.10.0
#
# Author:   Taylor Peters
#
# Purpose:  Utilize recently taught Python concepts.  

import random

#Initalizes starting round environment
def start(score=0, runningScore=0, par=0, runningPar=0, holeNum=1, name=""):
    name = describe_game(name)
    #Grabs new name, or runs alternative path for repeat player

    score, runningScore, par, runningPar, holeNum, name = golf(
        score, runningScore, par, runningPar, holeNum, name)
        #initializes new game of 'golf'


def describe_game(name):
    if name != "":
        print("\nLet's play another round, {}!".format(name))
    else: #repeat player tree
        if name == "":
            name = input("\nWhat is your name? \n>>> ").capitalize()
            if name != "":
                print("\nWelcome, {}!".format(name))
                print(
                    "\nIn this game, you will play six randomly-generated holes on my golf course.")
    return name

#determines par of hole based on randomly generated length
def calcPar(length):
    if length >= 475:
        par = 5
    elif length >= 190:
        par = 4
    else:
        par = 3
    return par

def golf(score, runningScore, par, runningPar, holeNum, name):
    golfing = True
    length = random.randrange(75, 575)
    par = calcPar(length)

    #limits game to six rounds
    if holeNum == 7:
        print("Good round, {}\n".format(name))
        show_final(runningScore, runningPar)
        again(score, runningScore, par,
              runningPar, holeNum, name)
    print("\nYou walk up to Hole " + str(holeNum) + ", it is a par " + str(par) + ", " + str(length) + " yard hole")
    swing(score, holeNum, par, length, runningPar, runningScore, name)

    while golfing:        
        par = calcPar(length)        
        swing(score, holeNum, par, length, runningPar, runningScore, name)


def swing(score, holeNum, par, length, runningPar, runningScore, name):
        
    distanceLeft = length
    score = 0

    #checks if player is within "tap in" range (3 yards), randomly generates the shot distance based on a random int within a range
    while distanceLeft > 3:      
      
        choice = input(
            "\nSelect your club: \n\nDriver 250-350yds (D)\nLong Iron 125-250yds (L)\nShort Iron 50-125yds (S)\nWedge 15-50yds (W)\nPutter (P): \n").lower()

        if choice == "d":
            distance = random.randrange(250, 350)
            print("\nYou pull out your driver and send it " +
                str(distance) + " yards")
            

        elif choice == "l":

            distance = random.randrange(125, 250)
            print("\nYou pull out your long iron and send it " +
                str(distance) + " yards")
            

        elif choice == "s":
            distance = random.randrange(50, 125)
            print("\nYou pull out your short iron and send it swing smoothly " +
                str(distance) + " yards")
            

        elif choice == "w":
            distance = random.randrange(15, 50)
            print("\nYou pull out your wedge and chip " +
                str(distance) + " yards")
            

        elif choice == "p":
            distance = random.randrange(5, 15)
            print("\nYou pull out your putter and give it a tap " +
                str(distance) + " yards")

        #updates remaining distance based on shot, adds a stroke to the score
        distanceLeft = distanceLeft - distance
        score += 1

        #checks if ball has gone past the hole, if it has "turns" the player around
        if distanceLeft < -3:
            distanceLeft = (distanceLeft * -1)

        #checks if ball is within 6 yards of hole
        if distanceLeft <= 3 and distanceLeft >= -3:
            print("\n{}! You sunk it!".format(name))
            print("You took " + str(score) + " stroke(s)!")

            #caluclates par
            runningPar += (score - par)
            runningScore += score
            show_score(runningScore, score, holeNum, runningPar)
            holeNum += 1
            golf(score, runningScore, par, runningPar, holeNum, name)
            
            #removes dialogue on final hole
            if holeNum <6:
                print("On to the next hole!")


        else:     
            dist_left(distanceLeft)       


            

def dist_left(distanceLeft):
        print("\nYou are " + str(distanceLeft) + " yards away.")

def show_score(runningScore, score, holeNum, runningPar):
    print("\nYou shot a " + str(score) + " on Hole " + str(holeNum) + ".  You are at " + str(runningScore) + " stroke(s) total, shooting a " + str(runningPar) + " on the day!")

def show_final(runningScore, runningPar):
    print("\nYou finished with a " + str(runningScore) + ", shooting a " + str(runningPar) + " on the day!")


def again(score, runningScore, par,
          runningPar, holeNum, name):
        choice = input("\nDo you want to play another round? (Y/N) \n>>>:").lower()
        if choice == "y":
            score = 0
            runningScore = 0
            par = 0
            runningPar = 0
            holeNum = 1
            start(score, runningScore, par,
                  runningPar, holeNum, name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            quit()
        else:
            print("\nEnter 'Y' for 'YES' or 'N' for 'NO'") 


if __name__ == "__main__":
    start()
