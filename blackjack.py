#!/usr/bin/env python3
import csv
import random
import db

# function that displays information to the user
def title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

# function that gets money from csv file
def print_money():
    money = db.get_money()
    print(f"Money: {money}")
    bet_amount = float(input("Bet amount: "))
    amount_left = money - bet_amount
    db.write_money(amount_left)
    return bet_amount

# function that draws a random card from the deck and then removes it
def draw_card(deck):
    card = random.choice(deck)
    deck.pop(deck.index(card))
    return card

# function that gets the dealers hand
def get_dealers_hand(deck, dealers_hand):
    card = draw_card(deck)
    dealers_hand.append(card)
    return dealers_hand

# function that gets the players hand
def get_players_hand(deck, players_hand):
    card = draw_card(deck)
    players_hand.append(card)
    return players_hand

def check_win(player, hand):
    if player == "player":
        total = 0
        for card in hand:
            total += card[2]
        
        return total
    
    elif player == "dealer":
        total = 0
        for card in hand:
            total += card[2]

        return total

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
    bet_amount = print_money()
    money = db.get_money()

    dealers_hand = []
    players_hand = []

    deck = make_deck()

    dealers_hand = get_dealers_hand(deck, dealers_hand)
    print("\nDEALER'S SHOW CARD:")
    for card in dealers_hand:
        print(f"{card[1]} of {card[0]}")

    players_hand = get_players_hand(deck, players_hand)
    players_hand = get_players_hand(deck, players_hand)

    print("\nYOUR CARDS:")
    for card in players_hand:
        print(f"{card[1]} of {card[0]}")
    
    check_win("player", players_hand)

    while True:
        choice = input("\nHit or stand? (hit/stand): ").lower()
        total = 0
        if choice == "hit":
            players_hand = get_players_hand(deck, players_hand)
            print("\nYOUR CARDS:")
            for card in players_hand:
                print(f"{card[1]} of {card[0]}")
                total += card[2]

            if total >= 21:
                while check_win("dealer", dealers_hand) < 17:
                    dealers_hand = get_dealers_hand(deck, dealers_hand)
                
                players_total = 0
                for card in players_hand:
                    players_total += card[2]

                print("\nDEALER'S CARDS:")
                dealers_total = 0
                for card in dealers_hand:
                    print(f"{card[1]} of {card[0]}")
                    dealers_total += card[2]

                print(f"\nYOUR POINTS:   {players_total}")
                print(f"DEALER'S POINTS: {dealers_total}")

                if 21 >= players_total > dealers_total or players_total <= 21 and dealers_total > 21:
                    print("\nCongratulations. You win!")
                    money = (money + bet_amount) * 1.5
                    print(f"Money: {money}")
                    db.write_money(money)
                    break
            
                elif players_total < dealers_total < 21 or players_total > 21 and dealers_total > 21 or players_total > 21 and dealers_total <= 21:
                    print("\nSorry. You lose.")
                    money = db.get_money()
                    print(f"Money: {money}")
                    break

                elif players_total == dealers_total:
                    print("\nIt's a tie!")
                    money = money + bet_amount
                    print(f"Money: {money}")
                    db.write_money(money)
                    break
                break

        if choice == "stand":
            while check_win("dealer", dealers_hand) < 17:
                dealers_hand = get_dealers_hand(deck, dealers_hand)
                
            players_total = 0
            for card in players_hand:
                players_total += card[2]

            print("\nDEALER'S CARDS:")
            dealers_total = 0
            for card in dealers_hand:
                print(f"{card[1]} of {card[0]}")
                dealers_total += card[2]

            print(f"\nYOUR POINTS:   {players_total}")
            print(f"DEALER'S POINTS: {dealers_total}")

            if 21 >= players_total > dealers_total or players_total <= 21 and dealers_total > 21:
                print("\nCongratulations. You win!")
                money = (money + bet_amount) * 1.5
                print(f"Money: {money}")
                db.write_money(money)
                break
            
            elif players_total < dealers_total < 21 or players_total > 21 and dealers_total > 21 or players_total > 21 and dealers_total <= 21:
                print("\nSorry. You lose.")
                money = db.get_money()
                print(f"Money: {money}")
                break
            
            elif players_total == dealers_total:
                print("\nIt's a tie!")
                money = money + bet_amount
                print(f"Money: {money}")
                db.write_money(money)
                break
            break
        
# dunder method
if __name__ == "__main__":
    main()
6