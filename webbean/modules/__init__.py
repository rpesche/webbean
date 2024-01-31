from webbean.modules.beancount import Beancount
from webbean.modules.weboob import Weboob

MODULES = {
    "beancount": Beancount,
    "weboob": Weboob,
}

__ALL__ = [Beancount, Weboob]
