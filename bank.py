#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path
import argparse
import logging

from jinja2 import Environment, PackageLoader

from modules import MODULES

from modules.beancount import beancount
from modules.weboob import weboob

# To avoid lint error
beancount.do_nothing()
weboob.do_nothing()


def write_transactions(account_transactions):
    env = Environment(loader=PackageLoader('bank', 'resources/template'))
    template = env.get_template('beancount.jinja')

    cpp_ids = {cpp_id for cpp_id, _ in account_transactions}
    account_transactions = sorted(account_transactions, key=lambda x: x[1].date)

    print(template.render(account_transactions=account_transactions, cpp_ids=cpp_ids))


def main(args):

    for arg in args:
        pass


def parse_arguments(args):

    accounts = []
    for module in MODULES.ALL:
        files = args.__dict__[module] or []
        for filename in files:
            if not path.isfile(filename):
                logging.error(f"the file {filename} doesn' not exist")
                return False

            klass = eval(module)
            account = klass(filename)
            accounts.append(account)

    return accounts


def add_modules_arguments(parser):
    for module in MODULES.ALL:
        parser.add_argument(f'--{module}', nargs='*')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Synchronise account")
    add_modules_arguments(parser)

    args = parser.parse_args()

    accounts = parse_arguments(args)
    if not accounts:
        parser.print_help()
        exit()
    beancount_transactions = accounts[0].get_all_transactions()

    w = weboob("plop")
    weboob_transactions = w.get_all_transactions()

    res = set(weboob_transactions) - set(beancount_transactions)
    for transaction in res:
        print(transaction)
