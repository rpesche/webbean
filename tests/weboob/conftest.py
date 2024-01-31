from datetime import date
from decimal import Decimal
from unittest.mock import MagicMock

import pytest
from woob.capabilities.bank import Account, Transaction
from woob.core import Woob


class FakeAccount(Account):
    label = "Compte Bancaire"


class FakeBackend:
    def __init__(self, transactions=[], *args, **kwargs):
        self.transactions = transactions

    def iter_accounts(self, *args, **kwargs):
        return [FakeAccount()]

    def iter_history(self, *args, **kwargs):
        return self.transactions


def mock_weboob(monkeypatch, transactions):
    monkeypatch.setattr(
        Woob,
        "load_backends",
        MagicMock(return_value={"bp": FakeBackend(transactions)}),
    )


@pytest.fixture()
def no_transaction(monkeypatch):
    mock_weboob(monkeypatch, [])


@pytest.fixture()
def one_transaction(monkeypatch):
    tr = Transaction()
    tr.label = "plop"
    tr.amount = Decimal(85.5)
    tr.date = date(2023, 1, 1)
    mock_weboob(monkeypatch, [tr])
