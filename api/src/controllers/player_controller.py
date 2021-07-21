from http import HTTPStatus
from json.decoder import JSONDecodeError
from flask import request
from lib.response import Response
from lib.request_args import RequestArgs
from models.player import Player
from mongoengine.errors import DoesNotExist, FieldDoesNotExist, ValidationError
import json

class PlayerController():
    @staticmethod
    def get():
        try:
            entities=Player.objects.filter(**RequestArgs(request.args, Player))
            return Response(data=entities, status=HTTPStatus.OK)
        except DoesNotExist:
            return Response(status=HTTPStatus.NOT_FOUND)

    @staticmethod
    def get_one(id: str):
        entity=None
        try:
            entity=Player.objects.get(id=id)
            return Response(data=entity, status=HTTPStatus.OK)

        except (ValidationError, DoesNotExist) as e:
            return Response(status=HTTPStatus.NOT_FOUND)

    @staticmethod
    def delete_one(id: str):
        try:
            entity=Player.objects.get(id=id)
            entity.delete()
            return Response(status=HTTPStatus.OK)
        except (ValidationError, DoesNotExist) as e:
            return Response(status=HTTPStatus.NOT_FOUND)


    @staticmethod
    def create():
        try:
            entity=Player(**json.loads(request.data))
            entity.validate()
            entity.save()
            return Response(data=entity, status=HTTPStatus.CREATED)

        except (FieldDoesNotExist, ValidationError, TypeError, JSONDecodeError) as e:
            return Response(status=HTTPStatus.BAD_REQUEST) 


    @staticmethod
    def update_one(id: str):
        try:
            data=json.loads(request.data)

            try:
                del data["_id"]
            except KeyError:
                pass

            try:
                entity=Player.objects.get(id=id)
                for key in data.keys():
                    entity[key] = data[key] 

                entity.save()

                return Response(data=entity, status=HTTPStatus.OK)
                
            except (ValidationError, DoesNotExist):
                return Response(status=HTTPStatus.NOT_FOUND)

        except (FieldDoesNotExist, ValidationError, TypeError, JSONDecodeError, KeyError) as e:
            return Response(status=HTTPStatus.BAD_REQUEST)