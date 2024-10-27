import random

def play_game():
    choice = input("Choose a door (red or yellow): ").strip().lower()
    
    if choice == "red":
        number = int(input("Select a number from 1 to 5: "))
        if number in [1, 4]:
            user_numbers = []
            for _ in range(3):
                user_numbers.append(int(input("Enter a number from 1 to 100: ")))
            total_sum = sum(user_numbers)
            if 130 < total_sum < 1079:
                print("You win!")
            else:
                print("You lost.")
        else:
            print("You lost.")
    
    elif choice == "yellow":
        number = int(input("Select a number from 6 to 10: "))
        if number % 2 == 0:
            user_numbers = []
            for _ in range(3):
                user_numbers.append(int(input("Enter a number from 1 to 100: ")))
            total_sum = sum(user_numbers)
            if 130 < total_sum < 1079:
                print("You win!")
            else:
                print("You lost.")
        else:
            print("You lost.")
    
    else:
        print("Invalid choice. Please select either red or yellow.")

play_game()
