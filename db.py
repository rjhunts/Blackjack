import sys
def get_money():
    try:
        with open("money.txt", "r") as file:
            money = file.read()
            return float(money)
    except FileNotFoundError:
        print("Data file missing.")
        print("Exiting program.")
        sys.exit()

def write_money(amount_left):
    try:
        with open("money.txt", "w") as file:
            file.write(str(amount_left))
    except FileNotFoundError:
        print("Data file missing.")
        print("Exiting program.")
        sys.exit()
