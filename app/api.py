from flask_appbuilder.api import BaseApi, expose as expose_api
from app.models import Asset
from seidr.interfaces import SeidrApi, SQLAInterface
from app import appbuilder


class AssetApi(SeidrApi):
    resource_name = "assets"
    datamodel = SQLAInterface(Asset)
    allow_browser_login = True


appbuilder.add_api(AssetApi)    