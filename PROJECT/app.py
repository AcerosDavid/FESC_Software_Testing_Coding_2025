import os
from config import DevelopmentConfig, ProductionConfig

ENV = os.getenv("ENV", "development")

if ENV == "production":
    config = ProductionConfig()
else:
    config = DevelopmentConfig()

print("DEBUG:", config.DEBUG)
print("DB:", config.DATABASE_URI)
