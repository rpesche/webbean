

class Transaction:

    date = ""

    amount = ""

    account = ""

    def __init__(self, date=None, amount=None, account=None):
        self.date = date
        self.amount = amount
        self.account = account

    def __str__(self):
        return "{}: {}".format(self.date, self.amount)

    def __eq__(self, other):
        return self.date == other.date and self.amount == other.amount

    def __hash__(self):
        return hash((self.date, self.amount))
