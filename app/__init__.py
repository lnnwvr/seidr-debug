import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA, Model, IndexView
from flask_appbuilder.menu import Menu
from flask_migrate import Migrate
from seidr import Seidr, SeidrIndexView
import app.config
import sys


logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)
log = logging.getLogger(__name__)

app = Flask(__name__)

app.config.from_object(config)
app.config.from_pyfile('../dev_config.py', silent=True)
app.config.from_envvar('APP_CONFIG_PATH', silent=True)

db = SQLA(app)
migrate = Migrate(app, db)


index = SeidrIndexView if app.config.get("WEBAPP") else IndexView

appbuilder = AppBuilder(
    app=app,
    session=db.session,
    indexview=index,
)

seidr = Seidr(appbuilder)

from . import models, api

