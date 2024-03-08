import random

l=["Rock","Paper","Scissor"]

while True:
    print("---------------------------------")
    print("0-Rock,1-Paper,2-Scissor, Enter your choice : ",end='')

    uc=int(input())
    uo=l[uc]

    print("User has selected : ",uo)
    sc=(random.randint(0,2))

    so=l[sc]
    print("System has selected : ",so)

    result=""

    if uc==0:   # Rock
        if sc==0:
            result="Match is draw"
        elif sc==2:
            result="User own the match"
        else:
            result="System own the match"

    elif uc==1: #Paper

        if sc==1:
            result="Match is draw"
        elif sc==0:
            result="User own the match"
        else:
            result="System own the match"
    elif uc==2: #Scissor

        if sc==2:
            result="Match is draw"
        elif sc==1:
            result="User own the match"
        else:
            result="System own the match"

    print("**************************")
    print(result)
    print("**************************")

    resp=input()

    if resp=='q':
        break
