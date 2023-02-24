from random import randint as r

# randint will be used as the computer choice

def game():
    option = {'rock' : 0, 'paper' : 1, 'scissors' : 2}
    print("\nLet's play rock, paper, scissors! Enter 'quit' to stop playing")
    wins = 0
    losses = 0
    ties = 0
    while True:
        choice = input("\nDo you pick rock, paper, or scissors? ")
        choice = choice.lower()
        if choice in option.keys():
            player_choice = option.get(choice)
            computer_choice = r(0,2)
            for key, value in option.items():
                if computer_choice == option[key]:
                    computer_hand = key
                    break
            if player_choice == computer_choice:
                ties += 1
                print(f"\nYou picked {choice} and I picked {computer_hand}. It's a tie! ")
            elif (choice == 'rock' and computer_hand == 'scissors') or (choice == 'paper' and computer_hand == 'rock') or (choice == 'scissors' and computer_hand == 'paper'):
                wins += 1
                if (wins == 1) and (losses == 0):
                    print(f"\nYou picked {choice} and I picked {computer_hand}. You win! Best two out of three? ")
                else:
                    print(f"\nYou picked {choice} and I picked {computer_hand}. You win! ")
            else:
                losses += 1
                print(f"\nYou picked {choice} and I picked {computer_hand}. I win! ")
                pass 
        elif choice == 'quit':
            if (wins > 0) or (losses > 0) or (ties > 0):
                print(f"\nThank you for playing! You won {str(wins)} times, lost {str(losses)} times, and tied {str(ties)} times.")
            else:
                print("\nYou didn't want to play? Wow.")
            break
        else:
            print("\nWhile I applaud your creativity that's just not a valid option. ")
            
game()