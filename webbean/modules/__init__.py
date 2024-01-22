from webbean.modules.beancount import beancount
from webbean.modules.weboob import weboob

MODULES = {
    "beancount": beancount,
    "weboob": weboob,
}

__ALL__ = [beancount, weboob]
