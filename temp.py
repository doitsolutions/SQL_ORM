from validator import Validator
import psycopg2
from contextlib import contextmanager
# TODO: Create Class based orm for creating data scheme
# TODO: create postgres client
class Postgres:
    def __init__(self):
        self.db_pool = self.__create_pool()
        self.database = self.__db()


    def __create_pool(self):
        return psycopg2.pool.SimpleConnectionPool(1, 10,
            host=CONF.db_host,
            database=CONF.db_name, 
            user=CONF.db_user, 
            password=CONF.db_user,
            port=CONF.db_port,
            options=None
        )


    @contextmanager
    def __db(self):
        con = self.db_pool.getconn()
        cur = con.cursor()
        try:
            yield con, cur
        finally:
            cur.close()
            self.db_pool.putconn(con)

test = Validator(name={"value": "abe", "required": True, "type": int})
print(test.__dict__)
test = Validator(name={"value": "", "required": True})

db = Postgres()

with db.database as (connection, cursor):
    try:
        cursor.execute("""INSERT INTO table (fields)
VALUES (values) RETURNING id""")
        my_id = cursor.fetchone()
        rowcount = cursor.rowcount
        if rowcount == 1:
            connection.commit()
        else:
            connection.rollback()
    except psycopg2.Error as error:
        print('Database error:', error)
    except Exception as ex:
        print('General error:', ex)
