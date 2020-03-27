import requests
import argparse

from work import snap


def send_request(msg):
    url = 'http://localhost:8000/api/'
    entry = {'text': msg}

    response = requests.post(url, data = entry)
    
    print(response.status_code)
    print(response.text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'HH Handler')
    parser.add_argument('-m', '--msg', help = 'Send Journal Entry', dest = 'msg')
    parser.add_argument('-s', '--snap', help = 'See snapshot', dest = 'snap', action = 'store_true')
    args = parser.parse_args()
    
    if args.msg:
        send_request(args.msg)
    
    if args.snap:
        snap.get_current()
