from src.ORM import BaseModel, Field
from src.decorators import Database
from src.adapter import Postgres, Mongo

postgres = Postgres(uri="127.0.0.1")

@Database(postgres)
class User(BaseModel):
    Apple = Field(required=True, type=str)
    Pear = Field(required=True, type=str)

user = User()

user.insert(Apple="Yo",Pear="sup")