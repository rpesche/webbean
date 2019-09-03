
from jinja2 import Environment, PackageLoader


class Account:

    def __init__(self, filename):
        self.filename = filename

    def get_all_transactions(self):
        raise LookupError

    def do_nothing(self):
        pass

    def write_transactions(self, account_transactions):

        env = Environment(loader=PackageLoader('webbean',
                                               'resources/template'))
        template = env.get_template(self.resource_filename)

        account_transactions = sorted(account_transactions, key=lambda x: x.date)

        print(template.render(transactions=account_transactions))
