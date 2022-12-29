import psycopg2
#from contextlib import contextmanager
class Postgres():
    def __init__(self, uri):
        self.adapter = "postgres"
        self.uri = uri
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