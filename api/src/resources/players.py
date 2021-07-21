from http import HTTPStatus
from api import app
from controllers.player_controller import PlayerController
from flask import request

from lib.response import Response

resource_name='players'

@app.route(f"/{resource_name}", methods=['GET', 'POST'])
def handle():
    if request.method == "GET":
        return PlayerController.get()
    if request.method == "POST":
        return PlayerController.create()
    return Response(status=HTTPStatus.METHOD_NOT_ALLOWED)

@app.route(f"/{resource_name}/<id>", methods=['GET','PATCH', 'DELETE'])
def handle_one(id: str):
    if request.method == "GET":
        return PlayerController.get_one(id)
    if request.method == "PATCH":
        return PlayerController.update_one(id)
    if request.method == "DELETE":
        return PlayerController.delete_one(id)
    return Response(status=HTTPStatus.METHOD_NOT_ALLOWED)
