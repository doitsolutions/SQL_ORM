from src.ORM import BaseModel, Field

class User(BaseModel):
    Apple = Field(required=True, type=str)
    Pear = Field(required=False, type=str)

user = User()

user.update(Pear="a")