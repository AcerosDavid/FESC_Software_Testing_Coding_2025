import os

class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = "sqlite:///default.db"

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = "sqlite:///dev.db"

class ProductionConfig(Config):
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///prod.db")
