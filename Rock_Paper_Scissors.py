
import random

p = 0
c = 0 
  
def rps(player, comp):
    global c
    global p
    if player == "Rock" and comp == "Rock":
        print("The computer chose rock too, Its a Tie!")
    if player == "Rock" and comp == "Paper":
        print("The computer chose paper, you lose! ")
        c = c + 1
    if player == "Rock" and comp == "Scissors":
        print("The computer chose scissors, you win! ")
        p = p + 1
    if player == "Paper" and comp == "Rock":
        print("The computer chose rock, you win! ")
        p = p + 1
    if player == "Paper" and comp == "Paper":
        print("The computer chose paper too, Its a tie! ")
    if player == "Paper" and comp == "Scissors":
        print("The computer chose scissors, you lose! ")
        c = c + 1
    if player == "Scissors" and comp == "Rock":
        print("The computer chose rock, you lose! ")
        c = c + 1
    if player == "Scissors" and comp == "Paper":
        print("The computer chose paper, you win! ")
        p = p + 1
    if player == "Scissors" and comp == "Scissors":
        print("The computer chose scissors too, Its a tie! ")

print("------------------------------------") 
print(" LETS PLAY ROCK, PAPER, SCISSORS!!! ")
print("------------------------------------")

while True:

    i = random.randint(1,3)
    if i == 1:
        h = "Rock"
    if i == 2:
        h = "Paper"   
    if i == 3:
        h = "Scissors"

    pick = str(input("Make your pick! "))
    if "Rock" in pick or "rock" in pick:
        x = "Rock"
            
    elif "Paper" in pick or "paper" in pick:
        x = "Paper"
            
    elif "Scissors" in pick or "scissors" in pick:
        x = "Scissors"
    elif "No" in pick or "no" in pick or "Quit" in pick or "quit" in pick:
        if c != 1 and p != 1:
            print("Okay, you won " + str(p) + " times and the computer won " + str(c) + " times")
        elif c != 1 and p == 1:
            print("Okay, you won " + str(p) + " time and the computer won " + str(c) + " times")
        elif c == 1 and p != 1:
            print("Okay, you won " + str(p) + " times and the computer won " + str(c) + " time")
        elif c == 1 and p == 1:
            print("Okay, you both won 1 time ")
        break
    else:
        print("Please input rock, paper, or scissors only!")
        print(" ")
        continue
        
    rps(x, h)
    print(" ")