from sqlorm import *

postgres = Postgres(uri="127.0.0.1")

@Database(postgres)
class User(BaseModel):
   name = Field(required=True, type=str)

user = User()

user.insert(name=1)