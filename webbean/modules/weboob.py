from woob.core import Woob

from webbean.core.account import Account
from webbean.core.transaction import Transaction


class Weboob(Account):
    def _get_all_transactions(self):
        weboob = Woob()
        backend = weboob.load_backends(names=["bp"])["bp"]  # TODO Make it generic

        account_transactions = []
        for account in backend.iter_accounts():
            if account.label != "Compte Bancaire":  # TODO Make it generic
                continue
            for weboob_transaction in backend.iter_history(account):
                transaction = Transaction(
                    date=weboob_transaction.date,
                    amount=float(weboob_transaction.amount),
                    label=weboob_transaction.label,
                )
                account_transactions.append(transaction)
        return account_transactions
