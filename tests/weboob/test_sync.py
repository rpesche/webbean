from freezegun import freeze_time

from webbean.modules.weboob import Weboob


def test_sync(no_transaction):
    woob = Weboob(None)
    transactions = woob.get_all_transactions(days_synced=30)
    assert transactions == []


@freeze_time("2023-01-05")
def test_one_transaction(one_transaction):
    woob = Weboob(None)
    transactions = woob.get_all_transactions(days_synced=30)
    assert len(transactions) == 1
    tr = transactions[0]

    assert tr.label == "plop"
    assert tr.amount == 85.5


def test_transaction_too_old(one_transaction):
    woob = Weboob(None)
    transactions = woob.get_all_transactions(days_synced=30)
    assert len(transactions) == 0
