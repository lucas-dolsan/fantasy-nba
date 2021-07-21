
from models.base_model import BaseModel

from mongoengine.fields import StringField

class Player(BaseModel):
    name=StringField(required=True)
