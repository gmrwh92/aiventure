##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "thisshouldberandomcharatersaiventures"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
