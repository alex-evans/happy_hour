import os
from dotenv import load_dotenv
import pprint
import requests


pp = pprint.PrettyPrinter(indent = 4)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
key = os.getenv('TRELLO_KEY')
token = os.getenv('TRELLO_TOKEN')

def get_current():
    boards_url = f'https://api.trello.com/1/members/alexevans28/boards'
    params = {
        'filter': 'all',
        'fields': 'all',
        'lists': 'none',
        'memberships': 'none',
        'organization': 'false',
        'organization_fields': 'name,displayName',
        'key': key,
        'token': token
    }

    resp = requests.request('GET', boards_url, params = params)
    pp.pprint(resp.text)