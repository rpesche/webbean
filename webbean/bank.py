#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path
import argparse
import logging


from webbean.modules import MODULES

from webbean.modules.beancount import beancount  # noqa
from webbean.modules.weboob import weboob  # noqa


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


def main():
    parser = argparse.ArgumentParser(description="Synchronise account")
    add_modules_arguments(parser)

    args = parser.parse_args()

    accounts = parse_arguments(args)
    if not accounts:
        parser.print_help()
        exit()
    beancount_transactions = accounts[0].get_all_transactions()

    w = weboob("plop")
    # TODO login password from config file
    weboob_transactions = w.get_all_transactions(login, password)

    missing_transactions = set(weboob_transactions) - set(beancount_transactions)
    accounts[0].write_transactions(list(missing_transactions))


if __name__ == '__main__':
    main()
