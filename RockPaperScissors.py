# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

def comp(move1, move2):
    if(move1 == move2):
        print("It's a tie!")
    elif(move1 == "rock"):
        if(move2 == "scissors"):
            return True
        else:
            return False
    elif(move1 == "paper"):
        if(move2 == "rock"):
            return True
        else:
            return False
    elif(move1 == "scissors"):
        if(move2 == "paper"):
            return True
        else:
            return False

print("Welcome to Rock-Paper-Scissors! This is a 2-player game. Input your moves.")
p1 = input("Player 1: ")
p2 = input("Player 2: ")
if(p1,p2 != "rock","paper","scissors"):
    