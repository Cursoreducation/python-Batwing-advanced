class Config:
    DEBUG = True
    ENV = 'development'


class DevConfig(Config):
    pass


class ProdConfig(Config):
    DEBUG = False
    ENV = 'production'
