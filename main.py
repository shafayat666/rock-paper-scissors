from random import choice
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
arts = [rock, paper, scissors]

def continue_game():
    choice = input("Do you want to play again? Type \"yes\" or \"no\".").lower()

    if choice == "yes":
        return True
    elif choice == "no":
        print("Thank you for playing Rock, Paper, Scissor.")
        return False
    else:
        print("Please type either \"yes\" or \"no\".")
        continue_game()

def user_input():
    try:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    except ValueError:
        print("Invalid input. Please type 0, 1 or 2.")
        return user_input()

    return user_choice


game_is_on = True
while game_is_on:

    user_choice = user_input()
    computer_choice = choice([0, 1, 2])

    print(f"You chose:\n{arts[user_choice]}")
    print(f"Computer chose:\n{arts[computer_choice]}")


    if user_choice == computer_choice:
        print("It's a draw.")
    # User chooses Rock
    elif user_choice == 0:
        if computer_choice == 1:
            print("You lose.")
        elif computer_choice == 2:
            print("You won!")
    # User chooses Paper
    elif user_choice == 1:
        if computer_choice == 0:
            print("You won!.")
        elif computer_choice == 2:
            print("You lose.")
    # User chooses Scissors
    elif user_choice == 2:
        if computer_choice == 1:
            print("You win!")
        elif computer_choice == 0:
            print("You lose.")

    if continue_game():
        game_is_on = True
    else:
        game_is_on = False