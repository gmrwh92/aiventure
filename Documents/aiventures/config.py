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
