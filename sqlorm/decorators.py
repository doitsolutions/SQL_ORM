from .drivers import DatabaseDriver
def Database(driver: DatabaseDriver):
    """
    Decorator to initialize database connection within the created validation model
    """
    def Model(cls):
        cls.database = driver
        return cls
    return Model