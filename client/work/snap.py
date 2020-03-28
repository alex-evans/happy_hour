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
        'fields': 'name',
        'lists': 'none',
        'memberships': 'none',
        'organization': 'false',
        'organization_fields': 'name,displayName',
        'key': key,
        'token': token
    }
    resp = requests.request('GET', boards_url, params = params)
    return json.loads(resp.text)


def get_hh_lists(board_id):
    lists_url = f'https://api.trello.com/1/boards/{board_id}/lists'
    params = {
        'filter': 'all',
        'fields': 'name,closed',
        'key': key,
        'token': token
    }
    resp = requests.request('GET', lists_url, params = params)
    trello_lists = json.loads(resp.text)
    hh_lists = []
    for t_list in trello_lists:
        if t_list['closed']:
            continue
        list_dict = {
            'id': t_list['id'],
            'name': t_list['name']
        }
        hh_lists.append(list_dict)
    return hh_lists


def get_cards(hh_lists, list_name):
    hh_list = [hh_list for hh_list in hh_lists if hh_list['name'] == list_name][0]
    hh_list_id = hh_list['id']
    cards_url = f'https://api.trello.com/1/lists/{hh_list_id}/cards'
    params = {
        'filter': 'all',
        'fields': 'id,name,due,dueComplete',
        'key': key,
        'token': token
    }
    resp = requests.request('GET', cards_url, params = params)
    list_cards = json.loads(resp.text)
    pp.pprint(list_cards)


def get_current():
    boards = get_all_boards()
    hh_board = [board for board in boards if board['name'] == 'HH'][0]
    if not hh_board:
        pp.pprint('No Happy Hour Board Found')
        return
    hh_lists = get_hh_lists(hh_board['id'])
    to_do_cards = get_cards(hh_lists, 'To Do:')
    this_week_cards = get_cards(hh_lists, 'This Week:')
    doing_cards = get_cards(hh_lists, 'Doing:')
    done_this_week_cards = get_cards(hh_lists, 'Done This Week:')
    
