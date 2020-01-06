# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock


def comp(move1, move2):
    if move1 == move2:
        return 0
    elif move1 == "rock":
        if move2 == "scissors":
            return 1
        else:
            return -1
    elif move1 == "paper":
        if move2 == "rock":
            return 1
        else:
            return -1
    elif move1 == "scissors":
        if move2 == "paper":
            return 1
        else:
            return -1

print("Welcome to Rock-Paper-Scissors! This is a 2-player game. Input your moves.")
q = "" #input if users want to quit
while q != "quit":
    p1 = input("Player 1: ")
    p2 = input("Player 2: ")
    while(not(p1 == "rock" or p1 == "paper" or p1 == "scissors" or
            p2 == "rock" or p2 == "paper" or p2 == "scissors")):
        print("Someone picked a nonexistent move! Pick again.")
        p1 = input("Player 1: ")
        p2 = input("Player 2: ")
    if(comp(p1,p2) == 1):
        print("Player 1 wins!")
    elif(comp(p1,p2) == -1):
        print("Player 2 wins!")
    else:
        print("It's a tie!")
    print("Enter 'quit' to quit. Enter anything else to play again.")
    q = input()
print("Thanks for playing!")