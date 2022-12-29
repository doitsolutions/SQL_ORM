def Database(database):
    def Model(cls):
        cls.database = database
        return cls
    
    return Model