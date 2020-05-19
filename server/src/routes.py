
from flask import request
from flask import current_app as app

from .models import db

from .handlers import lists
from .handlers import cmd_print
from .handlers import tasks
from .handlers import users


@app.route('/user/<username>')
def handle_user(username, methods=['GET']):
    return users.get_user(username)


@app.route('/tasks/{id}', methods=['GET'])
def handle_task(task_id):
    return tasks.get_task(task_id)


@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'POST':
        return tasks.save_task(db, request)
    else:
        return tasks.get_tasks()


@app.route('/lists', methods=['GET', 'POST'])
def handle_lists():
    from src import db
    if request.method == 'POST':
        return lists.save_list(db, request)
    else:
        return lists.get_lists()


@app.route('/start_day')
def handle_start_day():
    return cmd_print.start_data


@app.route('/')
def base():
    return 'Hello - no action taken'
