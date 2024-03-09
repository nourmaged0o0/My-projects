# File: CS112_A1_T2_3_20230446.py
# Purpose:
"""This is a two-player mathematical game of strategy. It is played by two
 people with a pile of coins (or other tokens) between them. The players take turns removing
 coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, ...).
 The player who removes the last coin wins."""
# Author: Nour Maged Mahmoud Abdel-Aal
# ID: 20230446

import random
import math

#to play again if players decide to play another round
def Play_again():
    their_choice2 =input("Do you want to play again? (y/n): ").upper()
    while their_choice2!= "Y" and their_choice2!="N":#to check if players choose a valid choice
        their_choice2= input("please enter a valid choice").upper()
    if their_choice2=="Y":
        the_game()
    else:
        exit()

#to check if any player won the game
def win(coins_num):
    if coins_num < 1:
        return True


def the_game():
    # ask user to choose if want a generated number of enter a number
    their_choice = input("A) Generate a random number\nB) Enter a number\n").upper()
    while their_choice != "A" and their_choice != "B": # to make sure that user choose a right choice
        print("invalid choice")
        their_choice = input("A) Generate a random number\nB) Enter a number\n").upper()
    if their_choice == "A":
        # 144 % 12 = 0
        # 155 % sqrt(155) != 0
        coins_num = random.randrange(100, 500)  # to choose a random number for coins
        while coins_num % math.sqrt(coins_num) == 0 : # to make sure that the generated number isn't perfect square number
            coins_num = random.randrange(100, 500)
    else:
        while True:
            try: #ac b safsdfasd 4.9
                coins_num = int(input("Enter a number between 10 and 1000 to start: ")) #ask user to enter a number of coins
                while coins_num % math.sqrt(coins_num) == 0 or coins_num<=10 or coins_num>=1000 : # to make sure that the generated number isn't perfect square or out of range
                    coins_num = int(input("invalid number\nplease Enter a number between 10 and 1000 to start: "))
                break
            except ValueError:  # runs if user entered a non-integer value
                print("Invalid input! Please enter a valid integer")
    print("coins:", coins_num)

    while True:
        try: #to catch if user enter a non integer value
            player1_num = int(input("player 1 Enter a number: "))
            #to make sure that the player1_num is perfect square using math lib
            # also to make sure that player1_num is positive and < coins_num
                                                                    #144 % 12=0
            while player1_num > coins_num or player1_num <= 0 or player1_num % math.sqrt(player1_num) != 0:
                player1_num = int(input("player 1 please Enter a valid number: "))
            coins_num = coins_num - player1_num #update coins status
            if win(coins_num):#check if the player won or not
                print("player 1 is the winner")
                Play_again()
                break
            else:
                print("coins:", coins_num)

            while True:
                try: #to catch if user enter a non integer value
                    player2_num = int(input("player 2 Enter a number: "))
                    # to make sure that the player2_num is perfect square using math lib
                    # also to make sure that player2_num is positive and < coins_num
                    while player2_num > coins_num or player2_num <= 0 or player2_num % math.sqrt(player2_num) != 0:
                        player2_num = int(input("player 2 please Enter a valid number: "))
                    coins_num = coins_num - player2_num #update coins status
                    if win(coins_num): #check if the player won or not
                        print("player 2 is the winner")
                        Play_again()
                        break
                    else:
                        print("coins:", coins_num)
                    break
                except ValueError: #runs if user entered a non-integer value
                    print("Invalid input! Please enter a valid integer for player 2.")
        except ValueError: #runs if user entered a non-integer value
            print("Invalid input! Please enter a valid integer for player 1.")


#this is the game description if players decide to read it
def game_description():
    print("You have a number of coins\nevery player remove a perfect square number (1,4,9,16....) from number of coins")
    print("the player who removes ths last coin wins the game")
    start_game_button=input("type Y to start the game: ").upper() #y
    while start_game_button!="Y":
        start_game_button = input("invalid choice please type Y to start the game: ").upper()
    the_game()

print("*** Welcome to Subtract Square Game ***")
their_choice1= input("A) Start the Game\nB) Game Description\n").upper() #a b A B
while their_choice1!="A" and their_choice1!="B": #to check if user enter a valid choice
    their_choice1 = input("Please Enter a valid choice\nA) Start the Game\nB) Game Description\n").upper()

if their_choice1=="A":
    the_game()
else:game_description()