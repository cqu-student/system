from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config.mysqlConfig import getMysqlConfig
from properties.commonVar import LOCAL

app = Flask(__name__)
db_config_local = getMysqlConfig(LOCAL)

db_local = f"mysql+pymysql://{db_config_local['user']}:{db_config_local['']}"