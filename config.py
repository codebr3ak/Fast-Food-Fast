# import os

# class Config:
#     '''
#     General configuration parent class
#     '''
#     SECRET_KEY = os.environ.get("SECRET_KEY")
#     CSRF_ENABLED = os.environ.get('CSRF_ENABLED')
#     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']




# class ProductionConfig(Config):
#     DEBUG = os.environ.get("DEBUG")


# class DevelopmentConfig(Config):
#     DEBUG = os.environ.get('DEBUG')


# class TestingConfig(Config):
#     TESTING = True


# config_options = {
#     'development': DevelopmentConfig,
#     'production': ProductionConfig,
#     'testing':TestingConfig,


# }


# import os

# class Config(object):
#     ...
#     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
# Your config.py file should now look like this:

import os
basedir = os.path.abspath(os.path.dirname(__file__))


<<<<<<< HEAD
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
=======
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get("SECRET_KEY")
    CSRF_ENABLED = os.environ.get('CSRF_ENABLED')
<<<<<<< HEAD
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
=======
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
>>>>>>> ba86ec7ade79a936b81e04ee8b80a97cf8f97770
>>>>>>> c6210a6f03e451f1b89fc05be33219256516393a


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
<<<<<<< HEAD
=======


config_options = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing':TestingConfig,


}
>>>>>>> ba86ec7ade79a936b81e04ee8b80a97cf8f97770
