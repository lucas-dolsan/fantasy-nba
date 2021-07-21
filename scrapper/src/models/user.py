from models.base_model import BaseModel
from mongoengine.fields import StringField

class User(BaseModel):
    name=StringField(required=True)
