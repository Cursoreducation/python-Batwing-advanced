class Config:
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = "postgresql://hello_flask:hello_flask@db:5432/hello_flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
