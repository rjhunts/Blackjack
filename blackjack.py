#!/usr/bin/env python3
import csv
import random

# function that displays information to the user
def title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

def players_hand():
    pass

def dealers_hand():
    pass

# function that generates the card deck
def get_deck():
    deck = []
    for x in range(4):
        if x == 0:
            suit = "spades"
        if x == 1:
            suit = "clubs"
        if x == 2:
            suit = "hearts"
        if x == 3:
            suit = "diamonds"
                                
        for value in range(13):
            if value == 0:
                rank = "ace"
            elif value == 10:
                rank = "jack"
                value = 9
            elif value == 11:
                rank = "queen"
                value = 9
            elif value == 12:
                rank = "king"
                value = 9
            else: rank = value+1

            card = [suit, rank, value+1]
            deck.append(card)

    return deck

# main function
def main():
    title()
    deck = get_deck()
    for count, card in enumerate(deck):
        print(card)
        
    print(f"There are {count+1} cards in the deck")

# dunder method
if __name__ == "__main__":
    main()
