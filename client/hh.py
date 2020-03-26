import requests


def send_request():
    url = 'http://localhost:8000/api/'
    entry = {'text': 'abcdefgh'}

    response = requests.post(url, data = entry)
    
    print(response.status_code)
    print(response.text)


if __name__ == '__main__':
    send_request()