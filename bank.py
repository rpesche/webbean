#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" WebBean synchro between bank and beancount file

Usage:
      bank.py <beancount_file> [--prefix] [--write]

Options:
    --prefix        Use custom prefix
    --write         Update the beancount file if differences are detected
"""

from docopt import docopt
from os import path
import logging



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
