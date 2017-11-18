from jinja2 import Environment, FileSystemLoader, select_autoescape
from beancount.loader import load_file as beancount_load_file
from beancount.core.data import Transaction as beancount_Transaction

from modules.Account import Account
from core.Transaction import Transaction


class beancount(Account):

    def get_all_transactions(self):

        res = beancount_load_file(self.filename)
        beancount_line = res[0]
        beancount_transactions = [line for line in beancount_line if isinstance(line, beancount_Transaction)]

        account_transactions = []
        for operation in beancount_transactions:
            for posting in operation.postings:
                if "Assets:CCP" in posting.account:
                    amount, _ = str(posting.units).split(" ")
                    transaction = Transaction(date=operation.date, amount=float(amount))
                    account_transactions.append(transaction)

        return account_transactions

    def write_transactions(self, transactions):
        env = Environment(loader=FileSystemLoader('resources/template/'))
        template = env.get_template('beancount.jinja')
        print(template.render(transactions=transactions))
