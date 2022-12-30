from .validator import Validator

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
        self.columns = {}
        
        for k in dir(self):
            v = getattr(self, k)
            if isinstance(v, Field):
                self.columns[k] = v.__dict__

    def __getitem__(self, key):
        return super().__getattribute__(key)

    def insert(self, **kwargs):
        for column in self.columns:
            Validator(column, self.columns[column], kwargs.get(column))
            
        print("done insert")
        
    def update(self, **kwargs):
        for column in kwargs:
            if column in self.columns:
                Validator(column, self.columns[column], kwargs.get(column))
            else:
                print("Invalid column")
                
        print("done update")