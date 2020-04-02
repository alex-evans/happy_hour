import os
import pprint
import json
from .trello import Trello


pp = pprint.PrettyPrinter(indent = 4)


def get_current():
    trello = Trello()
    pp.pprint('****************')
    print('')
    pp.pprint('DOING:')
    for card in trello.doing_cards:
        pp.pprint(card['name'])
    print('')
    pp.pprint('----')
    print('')
    pp.pprint('NEXT:')
    for card in trello.this_week_cards:
        pp.pprint(card['name'])
    print('')
    pp.pprint('****************')
