
from models.base_model import BaseModel
from mongoengine.fields import ReferenceField, StringField


class FantasyPlayer(BaseModel):
    name=StringField()
    player=ReferenceField('Player')
    fantasy_team=ReferenceField('FantasyTeam')
