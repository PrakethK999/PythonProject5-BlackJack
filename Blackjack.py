import random
from art import logo
user_cards = [random.randint(1, 10),random.randint(1, 10)]
computer_cards = [random.randint(1, 10),random.randint(1, 10)]

def get_sum(card_list):
    return sum(card_list)

def who_win():
    if get_sum(user_cards) > 21:
        print("You lose...")
    elif get_sum(computer_cards) > 21> get_sum(user_cards):
        print("You win!")
    elif 21 > get_sum(user_cards) > get_sum(computer_cards):
        print("You win!")
    elif get_sum(user_cards) < get_sum(computer_cards) < 21:
        print("You lose...")
    elif get_sum(user_cards) == get_sum(computer_cards):
        print("It's a draw!")

user_choice = input("Do you want to play a game of Blackjack? (y/n): ")
if user_choice == "y":
    print(logo)
    print(f"Your cards: {user_cards[0]}, {user_cards[1]}")
    print(f"Computer's first card: {computer_cards[0]}")
    user_choice = input("Type 'y' to get another card, or 'n' to pass.")
    if user_choice == "y":
        user_cards.append(random.randint(1, 10))
        print("Extra Cards: ", user_cards[2])
        print(f"Your cards: {user_cards[0]}, {user_cards[1]}, {user_cards[2]}")
        who_win()
    elif user_choice == "n":
        who_win()