def get_money():
    with open("money.txt", "r") as file:
        money = file.read()
        return money