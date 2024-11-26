#! /usr/bin/env python3
import db
import csv
import sys
import random

# prints out title and payout
def title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

# retrieves the deck from deck.csv file
def get_deck():
    try:
        with open("deck.csv") as file:
            reader = csv.reader(file)
            deck = [line for line in reader]
            return deck
        
    except FileNotFoundError:
        print("Could not find \"deck.csv\".")
        print("Exiting program.")
        sys.exit()

# draws a random card from the deck
def get_card(deck, hand, choose):
    card = random.choice(deck)
    deck.pop(deck.index(card))
    if choose and card[2] == "11":
        card = check_ace(card, hand)

    return card

# checks if the player draws an ace
def check_ace(card, hand):
    print(f"\nYou drew an {card[1]} of {card[0]}")
    while True:
        choice = input("Choose card value (1 or 11): ")
        if choice == "1" or choice == "11":
            card[2] = choice
            break
    
    # automatically chooses 1 if choosing 11 makes the player go over 21
    if get_points(hand) + 11 > 21:
        card[2] = "1"

    # automatically chooses 11 if choosing 11 results in 21 points for the player
    elif get_points(hand) + 11 == 21:
        card[2] = "11"

    return card

# prints the players / dealers cards
def print_cards(hand):
    for card in hand:
        print(f"{card[1]} of {card[0]}")

# prompts the user to buy chips
def buy_chips(money):
    while True:
        choice = input("Would you like to purchase more chips? (y/n): ")
        if choice == "y":
            while True:
                try:
                    new_money = int(input("Enter chip amount: "))
                    if new_money < 5 or new_money > 1000:
                        print("Chip amount must be at least 5 and no greater than 1000\n")
                    else:
                        db.write_money(new_money)
                        print(f"\nMoney: ${new_money}")
                        return new_money

                except ValueError:
                    print("Invalid chip amount, please try again.\n")

        elif choice == "n":
            print("\nCome back soon!")
            print("Bye!")
            sys.exit()
            break

        else:
            print("Invalid input, please try again.\n")

# validates the players money and retrives the bet amount
def get_bet(money):
    while True:
        try:
            bet_amount = float(input("Bet amount: $"))
            if bet_amount >= 5 and bet_amount <= 1000 and bet_amount <= money:
                return bet_amount
            else:
                print("Invalid bet amount, please try again.")

        except ValueError:
            print("Bet must be any number greater than or equal to $5\n")

# gets players choice for hit and stand
def hit_or_stand(players_hand, dealers_hand, deck):

    if get_points(players_hand) >= 21:
        while get_points(dealers_hand) < 17:
            dealers_hand.append(get_card(deck, dealers_hand, False))
        print("\nDEALER'S CARDS:")
        print_cards(dealers_hand)
        return False
    
    while True:
        choice = input("\nHit or stand? (hit/stand): ").lower()
        if choice == "hit":
            players_hand.append(get_card(deck, players_hand, True))
            print("\nYOUR CARDS:")
            print_cards(players_hand)
            return True
        elif choice == "stand":
            while get_points(dealers_hand) < 17:
                dealers_hand.append(get_card(deck, dealers_hand, False))
            print("\nDEALER'S CARDS:")
            print_cards(dealers_hand)
            return False
        else:
            print("Invalid choice, please try again.")

# gets the player and dealers points
def get_points(hand):
    points = 0
    for card in hand:
        points += int(card[2])
    return points

# decides who the winner is
def get_winner(players_hand, dealers_hand, money, bet, blackjack):
    players_points = get_points(players_hand)
    dealers_points = get_points(dealers_hand)
    print(f"\nYOUR POINTS:    {players_points}")
    print(f"DEALER'S POINTS: {dealers_points}")
    if blackjack:
        print("\nBLACKJACK!")
        print("\nYou win!")
        print(f"Money: ${round(money + (bet * 1.5), 2)}")
        db.write_money(round(money + (bet * 1.5), 2))
    elif players_points > dealers_points and players_points <= 21 or players_points <= 21 and dealers_points > 21:
        print("\nYou win!")
        print(f"Money: ${round(money + bet, 2)}")
        db.write_money(round(money + bet, 2))
    elif players_points < dealers_points and dealers_points <= 21 or players_points > 21:
        print("\nSorry. You lose.")
        print(f"Money: ${round(money - bet, 2)}")
        db.write_money(round(money - bet, 2))
    else:
        print("\nIt's a draw.")
        print(f"Money: ${round(money, 2)}")
        db.write_money(round(money, 2))

# checks for blackjack
def check_for_blackjack(players_hand, dealers_hand):
    players_points = get_points(players_hand)
    dealers_points = get_points(dealers_hand)
    if players_points == 21 and players_points != dealers_points:
        return True
    else:
        return False

# main function
def main():
    title()
    while True:
        money = db.get_money()
        print(f"Money: ${money}")
        if money < 5:
            money = buy_chips(money)
        deck = get_deck()
        random.shuffle(deck)
        bet = get_bet(money)
        db.write_money(money - bet)
        dealers_hand = []
        players_hand = []
        players_hand.append(get_card(deck, players_hand, True))
        dealers_hand.append(get_card(deck, dealers_hand, False))
        players_hand.append(get_card(deck, players_hand, True))
        dealers_hand.append(get_card(deck, dealers_hand, False))
        print("\nDEALER'S SHOW CARD:")
        print(f"{dealers_hand[0][1]} of {dealers_hand[1][0]}")
        print("\nYOUR CARDS")
        print_cards(players_hand)
        blackjack = check_for_blackjack(players_hand, dealers_hand)
        value = True
        while value:
            value = hit_or_stand(players_hand, dealers_hand, deck)
        get_winner(players_hand, dealers_hand, money, bet, blackjack)
        while True:
            choice = input("\nPlay again? (y/n): ").lower()
            if choice == "n":
                print("\nCome back soon!")
                print("Bye!")
                sys.exit()
            elif choice == "y":
                print()
                break
            else:
                print("Invalid input, please try again.")
                
# dunder method
if __name__ == "__main__":
    main()
