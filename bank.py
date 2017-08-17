#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" WebBean synchro between bank and beancount file

Usage:
      bank.py <beancount_file> [--prefix] [--write] [--add_header]

Options:
        --prefix      Use custom prefix
    --write           Update the beancount file if differences are detected
    --add_header      Add additional line to open account, initialise accounting, etc
"""

from weboob.core import Weboob
from jinja2 import Environment, PackageLoader, select_autoescape
from beancount.loader import load_file
from beancount.core.data import Transaction

from docopt import docopt
from os import path
import logging




def write_transactions( account_transactions ):
    env = Environment(loader=PackageLoader('bank', 'resources/template'))
    template = env.get_template('beancount.jinja')

    cpp_ids = { cpp_id for cpp_id, _ in account_transactions }
    account_transactions = sorted(account_transactions, key=lambda x: x[1].date)

    print(template.render( account_transactions=account_transactions, cpp_ids=cpp_ids ))



def get_all_bank_transactions():

    weboob = Weboob()
    backend = weboob.load_backends( names=['bp'] )['bp']
    backend.config['password'].set( "659333" )

    account_transactions = []
    for account in backend.iter_accounts():
        for transaction in backend.iter_history( account ):
           yield (account.id, transaction)


def get_all_accounting_transactions(beancount_file):
    res = load_file( beancount_file )
    beancount_line = res[0]
    beancount_transactions = [ line for line in beancount_line if isinstance(line, Transaction) ]

    # FOR ALL POSTING IN TRANSACTIONS => depense Assets
    account_transactions = []
    for transaction in beancount_transactions:
        for posting in transaction.postings:
            if "Assets:CCP-" in posting.account:
                account_transactions.append(posting)
    import pdb
    pdb.set_trace()





def main(args):
    beancount_file = args['<beancount_file>']

    if not path.isfile(beancount_file):
        logging.error( "file {} doesn't exist".format( beancount_file ) )
        return False

    if args['--prefix']:
        logging.debug("command --prefix is not implemented")
    if args['--write']:
        logging.debug("command --write is not implemented")





if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')
    main(arguments)
