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
def get_card(deck):
    card = random.choice(deck)
    deck.pop(deck.index(card))
    return card

# prints the players / dealers cards
def print_cards(hand):
    for card in hand:
        print(f"{card[1]} of {card[0]}")

# retrieves the players money from money.txt
def get_players_money():
    money = db.get_money()
    return money

# gets the players bet amount
def get_bet():
    while True:
        try:
            if bet_amount := int(input("Bet amount: ")) >= 5:
                return bet_amount
            else:
                print("Bet must be at least $5.\n")

        except ValueError:
            print("Bet must be a natural number greater than or equal to $5\n")

# gets players choice for hit and stand
def hit_or_stand(players_hand, dealers_hand, deck):
    while True:
        choice = input("\nHit or stand? (hit/stand): ").lower()
        if choice == "hit":
            players_hand.append(get_card(deck))
            print("\nYOUR CARDS:")
            print_cards(players_hand)
            return True
        elif choice == "stand":
            while get_points(dealers_hand) < 17:
                dealers_hand.append(get_card(deck))
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
def get_winner(players_hand, dealers_hand):
    players_points = get_points(players_hand)
    dealers_points = get_points(dealers_hand)
    print(f"\nYOUR POINTS:    {players_points}")
    print(f"DEALERS POINTS: {dealers_points}")
    if players_points > dealers_points and players_points <= 21 or players_points <= 21 and dealers_points > 21:
        print("\nYou win!")
    elif players_points < dealers_points and dealers_points <= 21 or dealers_points <= 21 and players_points > 21:
        print("\nSorry. You lose.")
    else:
        print("\nIt's a tie.")

# checks for blackjack
def check_for_blackjack(players_hand, dealers_hand):
    players_points = get_points(players_hand)
    dealers_points = get_points(dealers_hand)
    if players_points == 21 and players_points != dealers_points:
        print("\nBlackjack!")
        print("You win!")
        sys.exit()
    elif dealers_hand == 21 and dealers_points != players_points:
        print("\nDealers Blackjack")
        print("Sorry. You lose.")
        sys.exit()
    elif players_points == 21 and dealers_points == 21:
        print("\nDouble Blackjack")
        sys.exit()
    else: 
        return

# main function
def main():
    money = get_players_money()
    title()
    print(f"Money: {money}")
    deck = get_deck()
    bet = get_bet()
    dealers_hand = []
    players_hand = []
    dealers_hand.append(get_card(deck))
    players_hand.append(get_card(deck))
    dealers_hand.append(get_card(deck))
    players_hand.append(get_card(deck))
    print("\nDEALER'S SHOW CARD:")
    print(f"{dealers_hand[0][1]} of {dealers_hand[1][0]}")
    print("\nYOUR CARDS")
    print_cards(players_hand)
    check_for_blackjack(players_hand, dealers_hand)
    value = True
    while value:
        value = hit_or_stand(players_hand, dealers_hand, deck)
    winner = get_winner(players_hand, dealers_hand)

# dunder method
if __name__ == "__main__":
    main()
