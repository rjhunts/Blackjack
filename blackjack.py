#!/usr/bin/env python3
import csv
import random
import db

# function that displays information to the user
def title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

def print_money():
    money = db.get_money()
    print(f"Money: {money}")
    bet_amount = float(input("Bet amount: "))
    amount_left = money - bet_amount
    db.write_money(amount_left)

# function that draws a random card from the deck and then removes it
def draw_card(deck):
    card = random.choice(deck)
    return card

def get_dealers_hand(card, dealers_hand):
    dealers_hand.append(card)
    return dealers_hand

def get_players_hand(card, players_hand):
    players_hand.append(card)
    return players_hand

# function that generates the card deck
def make_deck():
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
    print_money()
    dealers_hand = []
    players_hand = []
    deck = make_deck()
    card = draw_card(deck)
    deck.pop(deck.index(card))
    dealers_hand = get_dealers_hand(card, dealers_hand)
    print("\nDEALER'S SHOW CARD:")
    print(f"{dealers_hand[0][1]} of {dealers_hand[0][0]}")
    card = draw_card(deck)
    deck.pop(deck.index(card))
    players_hand = get_players_hand(card, players_hand)
    card = draw_card(deck)
    deck.pop(deck.index(card))
    players_hand = get_players_hand(card, players_hand)
    print("\nYOUR CARDS:")
    print(f"{players_hand[0][1]} of {players_hand[0][0]}")
    print(f"{players_hand[1][1]} of {players_hand[1][0]}")
    choice = input("\nHit or stand? (hit/stand): ").lower()
    if choice == "hit":
        card = draw_card(deck)
        deck.pop(deck.index(card))
        players_hand = get_players_hand(card, players_hand)
        print("\nYOUR CARDS:")
        print(f"{players_hand[0][1]} of {players_hand[0][0]}")
        print(f"{players_hand[1][1]} of {players_hand[1][0]}")
        print(f"{players_hand[2][1]} of {players_hand[2][0]}\n")

# dunder method
if __name__ == "__main__":
    main()