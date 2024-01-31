from freezegun import freeze_time

from webbean.modules.beancount import Beancount


@freeze_time("2023-01-25")
def test_get_transaction_from_samples(beancount_sample_file):
    beancount = Beancount(beancount_sample_file)
    transactions = beancount.get_all_transactions(30)
    assert len(transactions) == 4


@freeze_time("2023-01-25")
def test_no_transaction_file(beancount_no_transaction_file):
    beancount = Beancount(beancount_no_transaction_file)
    transactions = beancount.get_all_transactions(30)
    assert len(transactions) == 0


@freeze_time("2023-01-25")
def test_no_transaction_on_ccp(beancount_no_transaction_on_ccp_file):
    beancount = Beancount(beancount_no_transaction_on_ccp_file)
    transactions = beancount.get_all_transactions(30)
    assert len(transactions) == 0
