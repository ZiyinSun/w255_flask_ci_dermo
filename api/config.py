import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "splite:///" + os.path.join(basedir, "prod.sqlite")

# class TestingConfig(Config):
  #  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "splite:///" + os.path.join(basedir, "prod.sqlite")

env_config = {
    "production": ProductionConfig,
    # "testing": TestingConfig,
}
