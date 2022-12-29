from src.ORM import BaseModel, Field

class User(BaseModel):
    Apple = Field(required=True, type=str)
    Pear = Field(required=True, type=str)

user = User()

user.insert(Apple="Wow")
user.update(Apple="haha")