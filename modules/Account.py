

class Account:
    filename = ""

    def __init__(self, filename):
        self.filename = filename

    def get_all_transactions(self):
        raise LookupError

    def do_nothing():
        pass

    def write_transactions(self, transactions):
        raise LookupError
