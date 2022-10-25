from app import app, db
from app.models import Asset, Unit
app.appbuilder.sm.add_user(
    "admin", "admin", "admin", "admin@for.bar", app.appbuilder.sm.find_role("Admin"), "admin"
)


db.create_all()
unit = Unit(name="unit1")
db.session.add(unit)
asset = Asset(name="asset1", owner=unit)
db.session.add(asset)
db.session.commit()

app.run(host="0.0.0.0", port=6060, debug=True)
