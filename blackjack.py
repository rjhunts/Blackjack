#!/usr/bin/env python3
import csv
import random
import db

# function that displays information to the user
def title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

def draw_card(deck):
    card = random.choice(deck)
    return card

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
    money = db.get_money()
    print(f"Money: {money}")
    bet_amount = int(input("Bet amount: "))
    deck = make_deck()
    show_card = draw_card(deck)
    deck.pop(deck.index(show_card))
    print(f"\nDEALER'S SHOW CARD:\n{show_card[1]} of {show_card[0]}")











    '''for count, card in enumerate(deck):
        print(card)
        
    print(f"There are {count+1} cards in the deck")'''

# dunder method
if __name__ == "__main__":
    main()
