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
