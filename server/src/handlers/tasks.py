
import json

from src.models import List
from src.models import Task
from src.models import User


# testing Hardcode user - future pull from a config or force logging it
USERNAME = 'admin'


def missing_required_data(task_data):
    if 'title' not in task_data:
        return 'title'
    if 'description' not in task_data:
        return 'description'
    if 'list' not in task_data:
        return 'list'
    return None


def save_task(db, request):
    if not request.json:
        return 'No Data to Save', 400

    missing_field = missing_required_data(request.json)
    if missing_field:
        return f'Missing Required Field: {missing_field}', 400

    user = User.query.filter_by(username=USERNAME).first()
    list_name = request.json['list']
    task_list = List.query.filter_by(name=list_name, user=user)
    if not task_list:
        return f'List Not Found: {list_name}'
    
    new_task = Task(
                    title=request.json['title'],
                    description=request.json['description'],
                    completed=False,
                    list=task_list
               )
    db.session.add(new_task)
    db.session.commit()

    return f'Task Created: {new_task.id}', 201


def get_task(task_id):
    if not task_id:
        return 'Missing Required Field: id', 400

    task = Task.query.filter_by(id=task_id).first()

    if not task:
        return f'Task Not Found: {task_id}'

    return json.dumps({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'due_date': task.due_date,
        'list': task.list
    })


def get_tasks():
    user = User.query.filter_by(username=USERNAME).first()
    lists = List.query.filter_by(user=user).all()

    tasks = []
    for user_list in lists:
        task = Task.query.filter_by(list=user_list).all()
        tasks.append({
            'task_id': task.id,
            'task_title': task.title
        })

    if len(tasks) == 0:
        return f'No Tasks Found for user: {user}'

    return json.dumps(tasks)
