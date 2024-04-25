# Christian Baker
# April 25th, 2024
# P5HW
# This is a menu driven program that will give the user options to add or subtract randomly generated numbers or to exit the program.

import random

def user_menu():
    print("Welcome to Math Quiz")
    print()
    print("MAIN MENU")
    print("---------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

def adding_random_numbers():
    firstnumber = random.randint(1, 1000)
    secondnumber = random.randint(1, 1000)
    result = firstnumber + secondnumber
    print(f"   {firstnumber}\n + {secondnumber}")
    how_many_guesses = 0
    while True:
        print()
        user_answer = int(input("Enter answer."))
        how_many_guesses += 1
        if user_answer == result:
            print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {how_many_guesses}")
            print()
            break
        elif user_answer < result:
            print("Sorry, guess is too low.\n\nTry again.")
        else:
            print("Sorry, guess is too high.\n\nTry again.")

def subtracting_random_numbers():
    firstnumber = random.randint(1, 1000)
    secondnumber = random.randint(1, 1000)
    result = firstnumber - secondnumber
    print(f"{firstnumber} - {secondnumber}")
    while True:
        user_answer = int(input("Enter the remainder:"))
        if user_answer == result:
            print()
            print("Congratulations!!!! Your answer is correct.")
            print()
            break
        else:
            print("Sorry, your answer is incorrect.\nTry again.")
            print()
            
def main():
    while True:
        user_menu()
        print()
        user_choice = input("Please choose one of the menu options: ")
        if user_choice == '1':
            adding_random_numbers()
        elif user_choice == '2':
            subtracting_random_numbers()
        elif user_choice == '3':
            print("Thank you for playing...\nBye!!")
            break
        else:
            print("The selection is invalid. Choose a number 1, 2, or 3.")

if __name__ == "__main__":
    main()
        
     
    
    
        
