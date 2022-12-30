import psycopg2


class DatabaseDriver():
    ...


class Postgres():
    def __init__(self, database: str = None, username: str = None, password: str = None, host: str = None, port: int = None, options: str = None):
        self.driver = "postgres"
        self.connection = self.connect(database, username, password, host, port, options)

    def connect(self, database: str = None, username: str = None, password: str = None, host: str = None, port: int = None, options: str = None):
        try:
            connection = psycopg2.connect(
                database=database, 
                user=username, 
                password=password, 
                host=host, 
                port=port,
                options=options
            )
            return connection.cursor()
        except psycopg2.Error as error:
            raise psycopg2.Error(f"{error}")
        except Exception as ex:
            raise Exception(f"{ex}")


class Mongo():
    def __init__(self, uri):
        self.uri = uri
        self.driver = "mongo"