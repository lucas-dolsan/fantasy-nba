
from models.base_model import BaseModel
from mongoengine.fields import StringField


class FantasyLeague(BaseModel):
    name=StringField(required=True)