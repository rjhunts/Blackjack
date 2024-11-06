def get_money():
    with open("money.txt", "r") as file:
        money = file.read()
        return float(money)

def write_money(amount_left):
    with open("money.txt", "w") as file:
        file.write(str(amount_left))