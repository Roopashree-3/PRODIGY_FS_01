import os

basedir=os.path.abspath(os.path.dirname(__file__))
DB_PATH=os.path.join(basedir,'instance','mydatabase.db')

SQLALCHEMY_DATABASE_URI=f"sqlite:///{DB_PATH}"
SQLALCHEMY_TRACK_MODIFICATIONS=False
