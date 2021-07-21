
from models.base_model import BaseModel
from mongoengine.fields import ReferenceField, StringField


class FantasyTeam(BaseModel):
    name=StringField(required=True)
    user=ReferenceField('User')
    fantasy_league=ReferenceField('FantasyLeague')