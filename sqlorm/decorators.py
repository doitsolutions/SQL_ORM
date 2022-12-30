from sqlorm.drivers import DatabaseDriver
def Database(driver: DatabaseDriver):
    def Model(cls):
        cls.database = driver
        return cls
    
    return Model