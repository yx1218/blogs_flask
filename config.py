import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.163.com')
    MAIL_PORT = os.environ.get('MAIL_PORT', '465')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'gaoqiang131218')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'QHBYCUXWEWANYSDM')
    BLOGS_MAIL_SUBJECT_PREFIX = '[Blogs]'
    BLOGS_MAIL_SENDER = 'BLOGS ADMIN'
    BLOGS_ADMIN = os.environ.get('BLOGS_ADMIN', 'gaoqiang131218@163.com')
    ADMIN = os.environ.get('ADMIN', '15002821218@163.com')



    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/blogs'


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {'development': DevelopmentConfig,
          'testing': TestingConfig,
          'production': ProductionConfig,
          'default': DevelopmentConfig}
