
from flask import Blueprint
from flask import request

from src.handlers import lists
from src.handlers import cmd_print
from src.handlers import tasks
from src.handlers import users


bp = Blueprint('server', __name__)


@bp.route('/user/<username>')
def handle_user(username, methods=['GET']):
    return users.get_user(username)


@bp.route('/tasks/{id}', methods=['GET'])
def handle_task(task_id):
    return tasks.get_task(task_id)


@bp.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    from src import db
    if request.method == 'POST':
        return tasks.save_task(db, request)
    else:
        return tasks.get_tasks()


@bp.route('/lists', methods=['GET', 'POST'])
def handle_lists():
    from src import db
    if request.method == 'POST':
        return lists.save_list(db, request)
    else:
        return lists.get_lists()


@bp.route('/start_day')
def handle_start_day():
    return cmd_print.start_data


@bp.route('/')
def base():
    return 'Hello - no action taken'
