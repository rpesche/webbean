
from weboob.core import Weboob

from modules.Account import Account
from core.Transaction import Transaction


class weboob(Account):

    def get_all_transactions(self):

        weboob = Weboob()
        backend = weboob.load_backends(names=['bp'])['bp']
        backend.config['password'].set("659333")

        account_transactions = []
        for account in backend.iter_accounts():
            for weboob_transaction in backend.iter_history(account):
                transaction = Transaction(date=weboob_transaction.date, amount=float(weboob_transaction.amount))
                account_transactions.append(transaction)
        return account_transactions