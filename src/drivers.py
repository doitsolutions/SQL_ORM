
class Postgres():
    def __init__(self, uri):
        self.uri = uri
        self.driver = "postgres"
    
class Mongo():
    def __init__(self, uri):
        self.uri = uri
        self.driver = "mongo"