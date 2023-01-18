import psycopg2
from psycopg2 import sql


class DatabaseDriver():
    """
    Default driver to handle typing for Database decorator
    """
    ...


class Postgres():
    """
    Postgres driver for connecting to a postgres database\n
    database - postgres database name\n
    username - username of account for postgres database\n
    password - password of account for postgres database\n
    host - host address for postgres database\n
    port - port for postgres database\n
    options - any other database options that may need to be supplied (i.e: schema, ect...)
    """
    def __init__(self, database: str = None, username: str = None, password: str = None, host: str = None, port: int = None, options: str = None):
        self.driver = "postgres"
        self.connection = self.connect(database, username, password, host, port, options)
        self.cursor = self.connection.cursor()

    def connect(self, database: str = None, username: str = None, password: str = None, host: str = None, port: int = None, options: str = None):
        """
        Function to handle connections to and from the postgres database\n
        database - postgres database name\n
        username - username of account for postgres database\n
        password - password of account for postgres database\n
        host - host address for postgres database\n
        port - port for postgres database\n
        options - any other database options that may need to be supplied (i.e: schema, ect...) 
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
            return connection

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
            fields = (*fields, sql.SQL(key))
            insert_values = (*insert_values, value)

        if schema:
            table = f"{schema}.{table}"


        sql_query = sql.SQL("INSERT INTO {table} ({fields}) VALUES {values} RETURNING *;").format(table=sql.SQL(table), fields=sql.SQL(', ').join(fields), values=sql.Literal(insert_values))

        try:
            self.cursor.execute(sql_query)
            self.connection.commit()
            return self.cursor.fetchone()

        except psycopg2.Error as error:
            self.cursor.execute("rollback")
            raise psycopg2.Error(f"{error}")

    def update(self, schema: str = None, table: str = None, query: dict = None, values: dict = None):
        """
        Function to handle updating data into a postgres table\n
        schema - schema in database\n
        table - table in database\n
        query - query of postgres search to find particular rows\n
        values - object of column:values to be inserted into postgres table
        """
        if not query:
            raise ValueError(f"No query for updating were supplied")

        if not isinstance(query, dict):
            raise TypeError(f"'query' must be of type: {dict} but instead found type: {type(query)}")

        if schema:
            table = f"{schema}.{table}"

        query = ' AND '.join([f"{key}{value}" for key, value in query.items()])
        values = ', '.join([f"{key}={value}" for key, value in values.items()])
        
        sql_query = sql.SQL("UPDATE {table} SET {values} WHERE {query} RETURNING *;").format(table=sql.SQL(table), values=sql.SQL(values), query=sql.SQL(query))

        try:
            self.cursor.execute(sql_query)
            self.connection.commit()
            return self.cursor.fetchone()

        except psycopg2.Error as error:
            self.cursor.execute("rollback")
            raise psycopg2.Error(f"{error}")

    def find_one(self, schema: str = None, table: str = None, query: dict = None, select: list = None):
        """
        Function to handle finding one row from a postgres table\n
        schema - schema in database\n
        table - table in database\n
        query - query of postgres search to find particular rows\n
        select - columns of postgres table selecting, defaults to '*'
        """
        if not isinstance(select, (list, type(None))):
            raise TypeError(f"'select' is not of type: {list} or type: {type(None)} instead found type: {type(select)}")

        if not query:
            raise ValueError("No query were supplied to be found with")

        if not isinstance(query, dict):
            raise TypeError(f"'query' is not of type: {dict} or type: {type(None)} instead found type: {type(query)}")

        if schema:
            table = f"{schema}.{table}"

        select = ', '.join(select) if select else '*'
        query = ' AND '.join([f"{key}{value}" for key, value in query.items()])

        sql_query = sql.SQL("SELECT {select} from {table} WHERE {query};").format(select=sql.SQL(select), table=sql.SQL(table), query=sql.SQL(query))

        try:
            self.cursor.execute(sql_query)
            self.connection.commit()
            return self.cursor.fetchone()

        except psycopg2.Error as error:
            self.cursor.execute("rollback")
            raise psycopg2.Error(f"{error}")

    def find_many(self, schema: str = None, table: str = None, query: str = None, select: tuple = '*'):
        """
        Function to handle finding many rows from a postgres table\n
        schema - schema in database\n
        table - table in database\n
        query - query of postgres search to find particular rows\n
        select - columns of postgres table selecting, defaults to '*'
        """
        if not isinstance(select, (list, type(None))):
            raise TypeError(f"'select' is not of type: {list} or type: {type(None)} instead found type: {type(select)}")

        if not query:
            raise ValueError("No query were supplied to be found with")

        if not isinstance(query, dict):
            raise TypeError(f"'query' is not of type: {dict} or type: {type(None)} instead found type: {type(query)}")

        if schema:
            table = f"{schema}.{table}"

        select = ', '.join(select) if select else '*'
        query = ' AND '.join([f"{key}{value}" for key, value in query.items()])
        
        sql_query = sql.SQL("SELECT {select} from {table} WHERE {query};").format(select=sql.SQL(select), table=sql.SQL(table), query=sql.SQL(query))

        try:
            self.cursor.execute(sql_query)
            self.connection.commit()
            return self.cursor.fetchall()

        except psycopg2.Error as error:
            self.cursor.execute("rollback")
            raise psycopg2.Error(f"{error}")

    def delete_one(self, schema: str = None, table: str = None, query: dict = None):
        """
        Function to handle deleting one row from a postgres table\n
        schema - schema in database\n
        table - table in database\n
        query - query of postgres search to find particular rows\n
        """
        if not query:
            raise ValueError("No query were supplied to be found with")

        if not isinstance(query, dict):
            raise TypeError(f"'query' is not of type: {dict} or type: {type(None)} instead found type: {type(query)}")

        if schema:
            table = f"{schema}.{table}"

        query = ' AND '.join([f"{key}{value}" for key, value in query.items()])

        sql_query = sql.SQL("DELETE FROM {table} WHERE {query} RETURNING *;").format(table=sql.SQL(table), query=sql.SQL(query))

        try:
            self.cursor.execute(sql_query)
            self.connection.commit()
            return self.cursor.fetchone()

        except psycopg2.Error as error:
            self.cursor.execute("rollback")
            raise psycopg2.Error(f"{error}")

    def delete_many(self, schema: str = None, table: str = None, query: dict = None):
        """
        Function to handle deleting many rows from a postgres table\n
        schema - schema in database\n
        table - table in database\n
        query - query of postgres search to find particular rows\n
        """
        if not query:
            raise ValueError("No query were supplied to be found with")

        if not isinstance(query, dict):
            raise TypeError(f"'query' is not of type: {dict} or type: {type(None)} instead found type: {type(query)}")

        if schema:
            table = f"{schema}.{table}"

        query = ' AND '.join([f"{key}{value}" for key, value in query.items()])
        
        sql_query = sql.SQL("DELETE FROM {table} WHERE {query} RETURNING *;").format(table=sql.SQL(table), query=sql.SQL(query))
        
        try:
            self.cursor.execute(sql_query)
            self.connection.commit()
            return self.cursor.fetchall()

        except psycopg2.Error as error:
            self.cursor.execute("rollback")
            raise psycopg2.Error(f"{error}")

    def execute(self, query: str = None):
        """
        Function to handle direct sql injection into postgres database\n
        query - direct sql query to postgres database
        """
        if not query:
            raise ValueError("No query were supplied to be found with")

        if not isinstance(query, str):
            raise TypeError(f"'query' is not of type: {str} instead found type: {type(query)}")

        try:
            self.cursor.execute(query)
            self.connection.commit()
            return self.cursor.fetchall()

        except psycopg2.Error as error:
            self.cursor.execute("rollback")
            raise psycopg2.Error(f"{error}")

    def execute_sql(self, query: str = None, values: tuple = None):
        """
        Function to handle direct sql injection into postgres database\n
        query - direct sql query to postgres database
        """
        if not query:
            raise ValueError("No query were supplied to be found with")

        if not isinstance(query, str):
            raise TypeError(f"'query' is not of type: {str} instead found type: {type(query)}")

        try:
            self.cursor.execute(query, (values,))
            self.connection.commit()
            return self.cursor.fetchall()

        except psycopg2.Error as error:
            self.cursor.execute("rollback")
            raise psycopg2.Error(f"{error}")


class Mongo():
    def __init__(self, uri):
        self.uri = uri
        self.driver = "mongo"