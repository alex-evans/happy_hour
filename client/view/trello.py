from dotenv import load_dotenv
from datetime import datetime
import os
import requests
import json


class Trello:
    def __init__(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        self.key = os.getenv('TRELLO_KEY')
        self.token = os.getenv('TRELLO_TOKEN')
        self.boards = self.get_all_boards()
        self.hh_board = self.get_hh_board()
        self.hh_lists = self.get_hh_lists()
        self.parking_lot_cards = self.get_cards('To Do:')
        self.this_week_cards = self.get_cards('This Week:')
        self.doing_cards = self.get_cards('Doing:')
        self.done_this_week_cards = self.get_cards('Done This Week:')
        self.done_this_month_cards = self.get_cards('Done This Month:')
        self.done_this_year_cards = self.get_cards('Done This Year:')

    def get_all_boards(self):
        boards_url = 'https://api.trello.com/1/members/alexevans28/boards'
        params = {
            'filter': 'all',
            'fields': 'name',
            'lists': 'none',
            'memberships': 'none',
            'organization': 'false',
            'organization_fields': 'name,displayName',
            'key': self.key,
            'token': self.token
        }
        resp = requests.request('GET', boards_url, params = params)
        return json.loads(resp.text)

    def get_hh_board(self):
        return [board for board in self.boards if board['name'] == 'HH'][0]

    def get_hh_lists(self):
        lists_url = f'https://api.trello.com/1/boards/{self.hh_board["id"]}/lists'
        params = {
            'filter': 'all',
            'fields': 'name,closed',
            'key': self.key,
            'token': self.token
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

    def get_cards(self, list_name):
        if list_name == 'Done This Month:':
            mnth = datetime.now().strftime('%B')
            list_name = f'Done {mnth}:'

        if list_name == 'Done This Year:':
            year = datetime.now().year
            list_name = f'Done {year}:'

        hh_list = [hh_list for hh_list in self.hh_lists if hh_list['name'] == list_name][0]
        hh_list_id = hh_list['id']
        cards_url = f'https://api.trello.com/1/lists/{hh_list_id}/cards'
        params = {
            'filter': 'all',
            'fields': 'id,name,due,dueComplete',
            'key': self.key,
            'token': self.token
        }
        resp = requests.request('GET', cards_url, params = params)
        return json.loads(resp.text)
