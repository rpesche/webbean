#!/usr/bin/python3

import argparse
import logging
from pathlib import Path

from webbean.modules import MODULES, weboob

DAYS_SYNCED = 30


def parse_arguments(args):
    accounts = []
    for module_name, module in MODULES.items():
        files = getattr(args, module_name, [])
        for filename in files:
            if not Path(filename).is_file():
                logging.error(
                    "the filename  doesn'nt exist",
                    extra={"account_filename": filename},
                )
                return False

            account = module(filename)
            accounts.append(account)

    return accounts


def add_modules_arguments(parser):
    for module in ["beancount"]:
        parser.add_argument(f"--{module}", nargs="*")


def main():
    parser = argparse.ArgumentParser(description="Synchronise account")
    add_modules_arguments(parser)

    args = parser.parse_args()

    accounts = parse_arguments(args)
    # if not accounts:
    # parser.print_help()
    # sys.exit()
    beancount_transactions = accounts[0].get_all_transactions(days_synced=DAYS_SYNCED)

    w = weboob.Weboob("plop")
    weboob_transactions = w.get_all_transactions(days_synced=DAYS_SYNCED)

    missing_transactions = []
    missing_transactions = [
        wb_transaction
        for wb_transaction in weboob_transactions
        if wb_transaction not in beancount_transactions
    ]

    accounts[0].write_transactions(list(missing_transactions))


if __name__ == "__main__":
    main()
