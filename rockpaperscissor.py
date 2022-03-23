import random
import time

user_wins = 0
bot_wins = 0

all_options = ['rock',
               'paper',
               'scissors']


while True:
    bot_choice = random.choice(all_options)

    user_choice = input("Rock, Paper or Scissors? Choose one! ").lower()
    while user_choice not in all_options:
        user_choice = input("That is not a valid choice, Please try again: ").lower()

    if user_choice == "rock":
        if bot_choice == "rock":
            print("Rock...")
            time.sleep(1)
            print("Paper...")
            time.sleep(1)
            print("Scissors...")
            time.sleep(1)
            print("Shoot!")
            print()
            print("You both chose {}, its a tie!".format(user_choice))
        elif bot_choice == "scissors":
            print("Rock...")
            time.sleep(1)
            print("Paper...")
            time.sleep(1)
            print("Scissors...")
            time.sleep(1)
            print("Shoot!")
            print()
            print("Your rock smashes scissors! YOU WIN!")
            user_wins += 1
        elif bot_choice == "paper":
            print("Rock...")
            time.sleep(1)
            print("Paper...")
            time.sleep(1)
            print("Scissors...")
            time.sleep(1)
            print("Shoot!")
            print()
            print("Paper covers rock! YOU LOSE!")
            bot_wins += 1
    elif user_choice == "paper":
        if bot_choice == "paper":
            print("Rock...")
            time.sleep(1)
            print("Paper...")
            time.sleep(1)
            print("Scissors...")
            time.sleep(1)
            print("Shoot!")
            print()
            print("You both chose {}, its a tie!".format(user_choice))
        elif bot_choice == "rock":
            print("Rock...")
            time.sleep(1)
            print("Paper...")
            time.sleep(1)
            print("Scissors...")
            time.sleep(1)
            print("Shoot!")
            print()
            print("Your paper covers rock! YOU WIN!")
            user_wins += 1
        elif bot_choice == "scissors":
            print("Rock...")
            time.sleep(1)
            print("Paper...")
            time.sleep(1)
            print("Scissors...")
            time.sleep(1)
            print("Shoot!")
            print()
            print("Scissors cuts through paper! YOU LOSE")
            bot_wins += 1
    elif user_choice == "scissors":
        if bot_choice == "scissors":
            print("Rock...")
            time.sleep(1)
            print("Paper...")
            time.sleep(1)
            print("Scissors...")
            time.sleep(1)
            print("Shoot!")
            print()
            print("You both chose {}, its a tie!".format(user_choice))
        elif bot_choice == "paper":
            print("Rock...")
            time.sleep(1)
            print("Paper...")
            time.sleep(1)
            print("Scissors...")
            time.sleep(1)
            print("Shoot!")
            print()
            print("Your scissors cuts through paper! YOU WIN")
            user_wins += 1
        elif bot_choice == "rock":
            print("Rock...")
            time.sleep(1)
            print("Paper...")
            time.sleep(1)
            print("Scissors...")
            time.sleep(1)
            print("Shoot!")
            print()
            print("Rock smashes scissors! YOU LOSE!")
            bot_wins += 1

    print()
    print("You have ",user_wins," wins.")
    print("The bot has ",bot_wins," wins.")
    print()

    repeat = input("Play again? (Y/N) ").lower()
    while repeat not in ['y', 'n']:
        repeat = input("That is not a valid choice. Please try again: ").lower()

    if repeat == 'n':
        break

print("\n----------------------------\n")





