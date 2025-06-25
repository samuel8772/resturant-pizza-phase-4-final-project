import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://sam:8772@localhost:5432/pizza_api_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False