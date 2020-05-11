
import json
from flask import request
from database import app
from database import User
from database import List
# from database import Task


# testing Hardcode user - future pull from a config or force logging it
USERNAME = 'admin'


######################
# USERS
######################


@app.route('/user/<username>')
def handle_user(username):
    user = User.query.filter_by(username=username).first()
    return f'{user}'


######################
# TASKS
######################


def save_task():
    return 'TODO - SAVE TASK'


def get_tasks():
    return 'TODO - GET TASKS'


@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'POST':
        return save_task()
    else:
        return get_tasks()


######################
# LISTS
######################


def save_list(req_data):
    print(req_data)
    return 'Ok', 200


def get_lists():
    user = User.query.filter_by(username=USERNAME).first()
    lists = List.query.filter_by(user=user)
    return {
        'test': 'lists'
    }


@app.route('/lists', methods=['GET', 'POST'])
def handle_lists():
    if request.method == 'POST':
        return save_list(request.data)
    else:
        return get_lists()


######################
# PRINTING
######################


@app.route('/start_day')
def handle_start_day():
    return ''


@app.route('/')
def base():
    return 'Hello - no action taken'


######################
######################


if __name__ == '__main__':
    app.run()
