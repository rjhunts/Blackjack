#!/usr/bin/env python3
import csv
import random
import db

# function that displays information to the user
def title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

# function that draws a random card from the deck and then removes it
def draw_card(deck):
    card = random.choice(deck)
    deck.pop(deck.index(card))
    return card
 
def get_players_hand(deck):
    return [draw_card(deck), draw_card(deck)]

def get_dealers_hand(deck):
    return [draw_card(deck), draw_card(deck)]

def bet_amount():
    print(f"Money: {db.get_money()}")
    bet = int(input("Bet amount: "))
    db.write_money(db.get_money()-bet)
    return bet

def print_cards(hand):
    for card in hand:
        print(f"{card[1]} of {card[0]}")
    print()

def hit(deck, players_hand):
    players_hand.append(draw_card(deck))
    print_cards(players_hand)

def check_win():
    pass

def get_total():
    pass

# function that generates the card deck
def get_deck():
    deck = []
    for x in range(4):
        if x == 0:
            suit = "Spades"
        if x == 1:
            suit = "Clubs"
        if x == 2:
            suit = "Hearts"
        if x == 3:
            suit = "Diamonds"
                                
        for value in range(13):
            if value == 0:
                rank = "Ace"
            elif value == 10:
                rank = "Jack"
                value = 9
            elif value == 11:
                rank = "Queen"
                value = 9
            elif value == 12:
                rank = "King"
                value = 9
            else: rank = value+1

            card = [suit, rank, value+1]
            deck.append(card)

    return deck

# main function
def main():
    title()
    deck = get_deck()
    dealers_hand = get_dealers_hand(deck)
    players_hand = get_players_hand(deck)
    bet = bet_amount()
    print("\nDEALER'S SHOW CARD:")
    print(f"{dealers_hand[0][1]} of {dealers_hand[1][0]}")
    print("\nYOUR CARDS:")
    print_cards(players_hand)
    while True:
        choice = input("Hit or stand? (hit/stand): ").lower()
        if choice == "hit":
            print("\nYOUR CARDS:")
            hit(deck, players_hand)
            break
        elif choice == "stand":
            print("\nDEALER'S CARDS:")
            print_cards(dealers_hand)
            print_cards(players_hand)
            break
        else:
            print("Invalid selection, please try again.\n")
    

# dunder method
if __name__ == "__main__":
    main()