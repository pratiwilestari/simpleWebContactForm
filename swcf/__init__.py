import psycopg2
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('settings.py')

def dbConnect():
    connection = psycopg2.connect(user=app.config['USER_DB'], password=app.config['PASS_DB'],
                    host=app.config['HOST_DB'], port=app.config['PORT_DB'], 
                    database=app.config['NAME_DB'])
    return connection

from swcf.controllers import index
