import csv
import os


class Portfolio:
    def __init__(self, portfolio_name):
        self.name = portfolio_name
        file_name = "coins.csv"
        fields = ["name", "ticker", "risk score"]
        self.coins_file = File(file_name).config(fields)

    def add_coin(self):
        coin = Coin.new()
        coins_dict = {"name": coin.name, "ticker": coin.ticker, "risk_score": coin.risk_score}
        with open(self.coins_file, "r", newline="") as coins_file:
            reader = csv.DictReader(coins_file)
            for row in reader:
                if row["name"] != coin.name:
                    raise ValueError("coin already exist")

        with open(self.coins_file, "a") as coins_file:
            writer = csv.DictWriter(coins_file, fieldnames=fieldnames)
            writer.writerow(coins_dict)


class File:
    def __init__(self, file_name):
        self.name = file_name

    def config(self, fields):
        if os.path.getsize(self.name) != 0:
            with open(self.name, "w") as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
        return self.name

    def read(self):
        row = []
        with open(self.name, "r") as f:
            reader = csv.DictReader(f)
            for i in reader:
                row.append(i)
        return row


class Coin:
    def __init__(self, coin_name, ticker="ticker", risk_score=3):
        self.name = coin_name
        self.ticker = ticker
        self.risk_score = risk_score

    @classmethod
    def new(cls):
        coin_name = "Cardano"
        ticker = "ADA"
        risk_score = 5
        return cls(coin_name, ticker, risk_score)


class Transactions:
    def __init__(self):
        self.file_name = "transactions.csv"
        self.fields = ["name", "transaction", "amount", "price"]
        self.file = File(self.file_name).config(self.fields)
        self.transaction = {}

    def buy(self, coin_name, amount, price):
        self.transaction = {"name": coin_name, "transaction": "buy", "amount": amount, "price": price}

    def sell(self, coin_name, amount, price):
        self.transaction = {"name": coin_name, "transaction": "sell", "amount": amount, "price": price}

    def save(self):
        with open(self.file, "a") as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            writer.writerow(self.transaction)

    def summary(self, coin_name):
        buys = []  # a nested list of all the buys and their respective B.P.
        sells = []  # a nested list of all the sells and their respective selling price
        balance = 0  # the amount of coins remaining
        investment = 0  # dollars used to buy the remaining coins
        total_buys = 0  # total cash used to buy coins
        total_sells = 0  # total cash made from selling coins

        with open(self.file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["name"] == coin_name:
                    amount = row["amount"]
                    price = row["price"]
                    if row["transactions"] == "buys":
                        buys.append([amount, price])
                        balance += amount
                        investment += (amount * price)
                    elif row["transactions"] == "sales":
                        sells.append([amount, price])
                        balance -= amount
                        investment -= (amount * price)

        print(investment)
        print(balance)
        try:
            average_bp = investment // balance
        except ZeroDivisionError:
            raise ValueError(f"{coin_name} balance missing")

        for i in buys:
            total_buys += i[0] * i[1]
        for i in sells:
            total_sells += i[0] * i[1]

        summary = {
            "name": self.name, "balance": balance,
            "investment": investment, "buying price": average_bp,
        }
        return summary



