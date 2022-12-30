from .validator import Validator
import inspect

# TODO: what about schemas? we need to accept them some how

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
        return super().__getattribute__(key)

    def __where(self):
        return inspect.stack()[1][3].upper()

    def insert(self, **kwargs):

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

        return self.database.insert(table=self.table, values=values)

    def update(self, query: dict = None, values: dict = None):
        # TODO: validation here

        return self.database.update(table=self.table, query=query, values=values)

        for column in kwargs:
            if column in self.columns:
                Validator(self.__where(), self.table, column, self.columns[column], kwargs.get(column))
            else:
                raise TypeError(f"{self.__where()} {self.table} -> '{column}' is not a valid column")
                
        print("done update")

    def find_one(self, select: list = None, query: dict = None):
        # TODO: validation here

        return self.database.find_one(select=select, table=self.table, query=query)

    def find_many(self, select: list = None, query: dict = None):
        # TODO: validation here

        return self.database.find_many(select=select, table=self.table, query=query)