from datetime import date

from beancount.core.data import Transaction


def beancount_transactions():
    return Transaction(date=date(2022, 1, 22), label=None, amount=455.38)
