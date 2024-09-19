
class Portfolio:
    def __init__(self, name):
        self.name = name
        self.coins = []

    def add_coin(self, name, ticker="ticker", risk_score=0):
        self.coins.append({"name": name, "ticker": ticker, "risk_score": risk_score})

    def remove_coin(self, name):
        for coin in self.coins:
            if coin["name"] == name:
                self.coins.pop(self.coins.index(coin))

    def save_changes(self):
        ...

    def stats(self):
        ...


class Transactions:
    def __init__(self):
        ...

    def buy_coin(self, name, quantity, value):
        ...

    def sell_coin(self, name, quantity, value):
        ...

    def save(self):
        ...

    def summary(self):
        ...


class Coin:
    def __init__(self, name, ticker="ticker", risk_score=0):
        self.name = name
        self.ticker = ticker
        self.risk_score = risk_score

    @classmethod
    def get(cls, name, ticker, risk_score):
        return cls(name, ticker, risk_score)
