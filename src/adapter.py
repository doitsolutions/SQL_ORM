
class Postgres():
    def __init__(self, uri):
        self.uri = uri
        self.adapter = "postgres"
    
class Mongo():
    def __init__(self, uri):
        self.uri = uri
        self.adapter = "mongo"