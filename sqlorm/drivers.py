import psycopg2


class DatabaseDriver():
    ...


class Postgres():
    def __init__(self, database: str = None, username: str = None, password: str = None, host: str = None, port: int = None, options: str = None):
        self.driver = "postgres"
        self.connection = self.connect(database, username, password, host, port, options)

    def connect(self, database: str = None, username: str = None, password: str = None, host: str = None, port: int = None, options: str = None):
        """
        Function to handle connections to and from the postgres database
        """
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

    def insert(self, table: str = None, fields: tuple = None, values: tuple = None):
        try:
            query = "INSERT INTO %s %s VALUES %s;"
            self.connection.execute(query, table, fields, values)
            return self.connection.fetchone()

        except psycopg2.Error as error:
            raise psycopg2.Error(f"{error}")

    def update(self, table: str = None, conditions: str = None, values: str = None):
        try:
            query="UPDATE %s SET %s WHERE %s;"
            self.connection.execute(query, table, values, conditions)
            return self.connection.fetchall()
        except psycopg2.Error as error:
            raise psycopg2.Error(f"{error}")

    def find_one(self, select: list = '*', table: str = None, conditions: tuple = None):
        try:
            query="SELECT %s FROM %s WHERE %s;"
            self.connection.fin(query, select, table, conditions)

        except psycopg2.Error as error:
            raise psycopg2.Error(f"{error}")

    def find_many(self):
        try:
        
            self.connection.execute(
                f"""
                INSERT INTO {table} {fields} VALUES {values};
                """
            )

        except psycopg2.Error as error:
            raise psycopg2.Error(f"{error}")

    def remove_one(self):
        try:
        
            self.connection.execute(
                f"""
                INSERT INTO {table} {fields} VALUES {values};
                """
            )

        except psycopg2.Error as error:
            raise psycopg2.Error(f"{error}")

    def remove_many(self):
        try:
        
            self.connection.execute(
                f"""
                INSERT INTO {table} {fields} VALUES {values};
                """
            )

        except psycopg2.Error as error:
            raise psycopg2.Error(f"{error}")


class Mongo():
    def __init__(self, uri):
        self.uri = uri
        self.driver = "mongo"