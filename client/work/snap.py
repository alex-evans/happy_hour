import os
from dotenv import load_dotenv
import pprint
import requests
import json


pp = pprint.PrettyPrinter(indent = 4)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
key = os.getenv('TRELLO_KEY')
token = os.getenv('TRELLO_TOKEN')


def get_all_boards():
    boards_url = 'https://api.trello.com/1/members/alexevans28/boards'
    params = {
        'filter': 'all',
        'fields': 'name,url',
        'lists': 'none',
        'memberships': 'none',
        'organization': 'false',
        'organization_fields': 'name,displayName',
        'key': key,
        'token': token
    }
    resp = requests.request('GET', boards_url, params = params)
    return json.loads(resp.text)


def get_hh_cards(hh_board_id):
    cards_url = f'https://api.trello.com/1/boards/{hh_board_id}/cards'
    params = {
        'fields': 'all',
        'key': key,
        'token': token
    }
    resp = requests.request('GET', cards_url, params = params)
    return json.loads(resp.text)


def get_current():
    boards = get_all_boards()
    hh_board = [board for board in boards if board['name'] == 'HH']
    if not hh_board:
        pp.pprint('No Happy Hour Board Found')
        return
    cards = get_hh_cards(hh_board[0]['id'])
    pp.pprint(cards)