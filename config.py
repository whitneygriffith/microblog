import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'guess'

#Called basedir in tutorial
DB_PATH = os.path.join(os.path.dirname(__file__), 'microblog.db')
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://yampeep@safepassage-mysqldbserver:sweetpotatoes@safepassage-mysqldbserver.mysql.database.azure.com/safepassage'.format(DB_PATH)

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

'''
Database admin login
u: admin1234
pw: @Qwerty1234
'''