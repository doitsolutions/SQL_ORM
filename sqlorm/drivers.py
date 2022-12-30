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

    def insert(self, schema: str = None, table: str = None, values: dict = None):
        """
        Function to handle inserting data into a postgres table\n
        schema - schema in database\n
        table - table in database\n
        values - object of column:values to be inserted into postgres table
        """
        fields = ()
        insert_values = ()

        if not values:
            raise ValueError(f"No columns or values were supplied to be inserted")

        if not isinstance(values, dict):
            raise TypeError(f"'values' must be of type: {dict} but instead found type: {type(values)}")

        for key, value in values.items():
            fields = (*fields, key)
            insert_values = (*insert_values, value)

        if schema:
            table = f"{schema}.{table}"

        query = "INSERT INTO %s %s VALUES %s;"

        try:
            
            self.connection.execute(query, table, fields, insert_values)
            return self.connection.fetchone()

        except psycopg2.Error as error:
            raise psycopg2.Error(f"{error}")

    def update(self, schema: str = None, table: str = None, conditions: dict = None, values: dict = None):
        """
        Function to handle updating data into a postgres table\n
        schema - schema in database\n
        table - table in database\n
        values - object of column:values to be inserted into postgres table
        """
        if not conditions:
            raise ValueError(f"No conditions for updating were supplied")

        if not isinstance(conditions, dict):
            raise TypeError(f"'conditions' must be of type: {dict} but instead found type: {type(conditions)}")

        if schema:
            table = f"{schema}.{table}"

        conditions = ' AND '.join([f"{key}={value}" for key, value in conditions.items()])
        values = ', '.join([f"{key}={value}" for key, value in values.items()])
        query="UPDATE %s SET %s WHERE %s;"

        try:
            self.connection.execute(query, table, values, conditions)
            return self.connection.fetchall()

        except psycopg2.Error as error:
            raise psycopg2.Error(f"{error}")

    def find_one(self, schema: str = None, table: str = None, conditions: dict = None, select: list = None):

        if not isinstance(select, (dict, type(None))):
            raise TypeError(f"'select' is not of type: {dict} or type: {type(None)} instead found type: {type(select)}")

        if not conditions:
            raise ValueError("No conditions were supplied to be found with")

        if not isinstance(conditions, dict):
            raise TypeError(f"'conditions' is not of type: {dict} or type: {type(None)} instead found type: {type(conditions)}")

        if schema:
            table = f"{schema}.{table}"

        select = tuple(select) if select else '*'
        conditions = ' AND '.join([f"{key}={value}" for key, value in conditions.items()])
        query="SELECT %s FROM %s WHERE %s;"

        try:
            self.connection.execute(query, select, table, conditions)
            return self.connection.fetchone()

        except psycopg2.Error as error:
            raise psycopg2.Error(f"{error}")

    def find_many(self, schema: str = None, table: str = None, conditions: str = None, select: tuple = '*'):

        if not isinstance(select, (dict, type(None))):
            raise TypeError(f"'select' is not of type: {dict} or type: {type(None)} instead found type: {type(select)}")

        if not conditions:
            raise ValueError("No conditions were supplied to be found with")

        if not isinstance(conditions, dict):
            raise TypeError(f"'conditions' is not of type: {dict} or type: {type(None)} instead found type: {type(conditions)}")

        if schema:
            table = f"{schema}.{table}"

        select = tuple(select) if select else '*'
        conditions = ' AND '.join([f"{key}={value}" for key, value in conditions.items()])
        query="SELECT %s FROM %s WHERE %s;"

        try:
            self.connection.execute(query, select, table, conditions)
            return self.connection.fetchall()

        except psycopg2.Error as error:
            raise psycopg2.Error(f"{error}")

    def delete_one(self, schema: str = None, table: str = None, conditions: dict = None):

        if not conditions:
            raise ValueError("No conditions were supplied to be found with")

        if not isinstance(conditions, dict):
            raise TypeError(f"'conditions' is not of type: {dict} or type: {type(None)} instead found type: {type(conditions)}")

        if schema:
            table = f"{schema}.{table}"

        conditions = ' AND '.join([f"{key}={value}" for key, value in conditions.items()])
        query = 'DELETE FROM %s WHERE %s'

        try:
            self.connection.execute(query, table, conditions)
            return self.connection.fetchone()

        except psycopg2.Error as error:
            raise psycopg2.Error(f"{error}")

    def delete_many(self, schema: str = None, table: str = None, conditions: dict = None):

        if not conditions:
            raise ValueError("No conditions were supplied to be found with")

        if not isinstance(conditions, dict):
            raise TypeError(f"'conditions' is not of type: {dict} or type: {type(None)} instead found type: {type(conditions)}")

        if schema:
            table = f"{schema}.{table}"

        conditions = ' AND '.join([f"{key}={value}" for key, value in conditions.items()])
        query = 'DELETE FROM %s WHERE %s'

        try:
            self.connection.execute(query, table, conditions)
            return self.connection.fetchall()

        except psycopg2.Error as error:
            raise psycopg2.Error(f"{error}")


class Mongo():
    def __init__(self, uri):
        self.uri = uri
        self.driver = "mongo"
