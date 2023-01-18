from .validator import Validator
import inspect

class Field():
    """
    Class to denote a field on the model - if not present, the class variable is not recognized as a valid model field
    """
    def __init__(cls, **kwargs):
        for k,v in kwargs.items():
            setattr(cls, k, v)

class BaseModel():
    """
    Base Model inhereted by created ORM class to validate fields passed and handles connectivity to database to execute upon
    """
    def __init__(self):
        # automatically passed from database decorator that sets self.database from driver passed
        self.database = self.database
        self.table = self.__class__.__name__
        self.columns = {}
        
        for k in dir(self):
            v = getattr(self, k)
            if isinstance(v, Field):
                self.columns[k] = v.__dict__

    def __getitem__(self, key):
        # TODO: write doc string here
        return super().__getattribute__(key)

    def __where(self):
        # TODO: write doc string here
        return inspect.stack()[1][3].upper()

    def insert(self, schema: str = None, **kwargs):
        """
        Function to handle insert functionality of all drivers\n
        schema - handles schema of database if present\n
        kwargs - columns, and key,value pair of columns being inserted
        """
        values = {}
        for column in kwargs:
            if column not in self.columns:
                raise TypeError(f"{self.__where()} {self.table} -> '{column}' is not a valid column")
            
        for column, constraints in self.columns.items():
            valid = Validator(self.__where(), self.table, column, self.columns[column], kwargs.get(column))

            if constraints.get('validate'):
                value = kwargs.get(column)
                validate = constraints['validate']

                validate(value)

            values[valid.column] = valid.value

        return self.database.insert(schema=schema, table=self.table, values=values)

    def update(self, schema: str = None, query: dict = None, values: dict = None):
        """
        Function to handle update functionality of all drivers\n
        schema - handles schema of database if present\n
        query - search parameters of database\n
        values - key, value pair of columns being updated
        """
        # TODO: validation here

        return self.database.update(schema=schema, table=self.table, query=query, values=values)

        for column in kwargs:
            if column in self.columns:
                Validator(self.__where(), self.table, column, self.columns[column], kwargs.get(column))
            else:
                raise TypeError(f"{self.__where()} {self.table} -> '{column}' is not a valid column")
                
        print("done update")

    def find_one(self, schema: str = None, select: list = None, query: dict = None):
        """
        Function to handle find one entry functionality of all drivers\n
        schema - handles schema of database if present\n
        select - columns you want to select from query (if not present all will be returned) \n
        query - search parameters of database
        """
        # TODO: validation here

        return self.database.find_one(schema=schema, select=select, table=self.table, query=query)

    def find_many(self, schema: str = None, select: list = None, query: dict = None):
        """
        Function to handle finding many entries functionality of all drivers\n
        schema - handles schema of database if present\n
        select - columns you want to select from query (if not present all will be returned) \n
        query - search parameters of database
        """
        # TODO: validation here

        return self.database.find_many(schema=schema, select=select, table=self.table, query=query)

    def delete_one(self, schema: str = None, query: dict = None):
        """
        Function to handle deleting one entry functionality of all drivers\n
        schema - handles schema of database if present\n
        query - search parameters of database
        """
        # TODO: validation here

        return self.database.delete_one(schema=schema, table=self.table, query=query)

    def delete_many(self, schema: str = None, query: dict = None):
        """
        Function to handle deleting many entries functionality of all drivers\n
        schema - handles schema of database if present\n
        query - search parameters of database
        """
        # TODO: validation here

        return self.database.delete_many(schema=schema, table=self.table, query=query)

    def execute(self, query: str = None):
        """
        Function to handle query language functionality of all drivers\n
        query - query operation for databse
        """
        # TODO: validation here

        return self.database.execute(table=self.table, query=query)

    def execute_sql(self, query: str = None, values: tuple = None):
        """
        Function to handle query language functionality of all drivers\n
        query - query operation for databse\n
        values - values of query to avoid sql injection if desired
        """
        # TODO: validation here

        return self.database.execute_sql(query=query, values=values)
