import psycopg2
from contextlib import contextmanager

from src.validator import Validator
class Postgres(Validator):
    def __init__(self):
        # self.db_pool = self.__create_pool()
        # self.database = self.__db()
        ...


    # def __create_pool(self):
    #     return psycopg2.pool.SimpleConnectionPool(1, 10,
    #         host=CONF.db_host,
    #         database=CONF.db_name, 
    #         user=CONF.db_user, 
    #         password=CONF.db_user,
    #         port=CONF.db_port,
    #         options=None
    #     )


    # @contextmanager
    # def __db(self):
    #     con = self.db_pool.getconn()
    #     cur = con.cursor()
    #     try:
    #         yield con, cur
    #     finally:
    #         cur.close()
    #         self.db_pool.putconn(con)



    def insert(self, obj: dict):
        print(obj)
        # Validator(kwargs)
        # with self.database as (connection, cursor):
        #     try:
        #         cursor.execute("""INSERT INTO table (fields)
        # VALUES (values) RETURNING id""")
        #         my_id = cursor.fetchone()
        #         rowcount = cursor.rowcount
        #         if rowcount == 1:
        #             connection.commit()
        #         else:
        #             connection.rollback()
        #     except psycopg2.Error as error:
        #         print('Database error:', error)
        #     except Exception as ex:
        #         print('General error:', ex)

class Field:

    def __init__(cls, **kwargs):
        for k, v in kwargs.items():
            print(k, v)
            setattr(cls, k, v)

class Test:

    def __init__(self, nm: str):
        self.name = Field(required=True, type=str, value=nm)

test = Test(nm="abe")
print(test.name.__dict__)
db = Postgres()
db.insert(test)