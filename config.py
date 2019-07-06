class Config:
    SECRET_KEY = '3b4c830cd7d88c05cfa5d6da59af4561'


class Development(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1:5432/june_payroll_system'
    DEBUG = True


class Production(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgres://rmkcdgvjxvodcn:ba198d1c400abd9b1933419eefbe75a4fab8b4b63f9b79e03c2868d5d193daab@ec2-23-21-160-38.compute-1.amazonaws.com:5432/deb7bfk1e0rkhd'

    DEBUG = False

