import random
player = ""
computer = ""

while player == computer:
    print("Rock, Paper, Scissors!")
    print("Rock Breaks Scissors, Scissors cuts paper, paper covers rock")
    player = input("Pick an Option (R for Rock,P for Paper,S for Scissors): ").upper()
    options = ['R','P','S']
    game_dict={
       'R':"Rock",
       'P':"Paper",
       'S':"Scissors"
    }

    computer = random.choice(options)
    

    while player not in options:
        print("Invalid input, pick again!")
        player = input("Pick an Option (R for Rock,P for Paper,S for Scissors): ").upper()
        
    player_word = game_dict.get(player)
    computer_word = game_dict.get(computer)

    print(f'Player ({player_word}) : CPU({computer_word})')

    if(player == computer):
        print("Tie")
    elif(player == "R"):
        if(computer == "P"):
            print("Computer Wins")
        if(computer == "S"):
            print("Player Wins")
    elif(player == "P"):
        if(computer == "S"):
            print("Computer Wins")
        if(computer == "R"):
            print("Player Wins")
    elif(player == "S"):
        if(computer == "R"):
            print("Computer Wins")
        if(computer == "P"):
            print("Player Wins")


    