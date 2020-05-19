
import json

from src.models import List
from src.models import User


# testing Hardcode user - future pull from a config or force logging it
USERNAME = 'admin'


def save_list(db, request):
    if not request.json:
        return 'No Data to Save', 400

    if 'name' not in request.json:
        return 'Missing Field: name', 400

    user = User.query.filter_by(username=USERNAME).first()
    new_list = List(name=request.json['name'], user=user)

    db.session.add(new_list)
    db.session.commit()

    return f'List Created: {new_list.id}', 201


def get_lists():
    user = User.query.filter_by(username=USERNAME).first()
    lists = List.query.filter_by(user=user).all()
    user_lists = []
    for item_list in lists:
        user_lists.append(item_list.name)
    return json.dumps(user_lists)
