from beancount.core.data import Open
from beancount.core.data import Transaction as beancount_Transaction
from beancount.loader import load_file as beancount_load_file

from webbean.core.transaction import Transaction
from webbean.modules.account import Account


class Beancount(Account):
    account_type_name = "beancount"
    resource_filename = "beancount.jinja"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.beancount_account = None

    def get_account(self):
        if self.beancount_account is None:
            self.beancount_account = beancount_load_file(self.filename)
        return self.beancount_account

    def _get_all_transactions(self):
        beancount_line = self.get_account()
        beancount_transactions = [
            line for line in beancount_line[0] if isinstance(line, beancount_Transaction)
        ]

        account_transactions = []
        for operation in beancount_transactions:
            for posting in operation.postings:
                if "Assets:CCP" in posting.account:
                    posting_date = operation.meta.get("real_date") or operation.date
                    amount, _ = str(posting.units).split(" ")
                    transaction = Transaction(date=posting_date, amount=float(amount))
                    account_transactions.append(transaction)

        return account_transactions

    def _get_account(self):
        for tr in self.get_account()[0]:
            if isinstance(tr, Open):
                yield tr.account
