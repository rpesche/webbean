from pathlib import Path

import pytest

RESOURCE_DIRECTORY = Path(__file__).parent / "resources"


@pytest.fixture()
def beancount_sample_file():
    return RESOURCE_DIRECTORY / "beancount" / "sample.beancount"


@pytest.fixture()
def beancount_no_transaction_file():
    return RESOURCE_DIRECTORY / "beancount" / "accounts.beancount"


@pytest.fixture()
def beancount_no_transaction_on_ccp_file():
    return RESOURCE_DIRECTORY / "beancount" / "no_transaction_on_ccp.beancount"
