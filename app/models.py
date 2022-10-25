

from flask_appbuilder import Model
from sqlalchemy import select, Column, Integer, String, ForeignKey, Boolean, Float, BigInteger, Date, DateTime, Enum, \
    UniqueConstraint, Table
from sqlalchemy.orm import relationship




class Asset(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(512), nullable=False)
    owner_id = Column(Integer, ForeignKey('unit.id'))
    owner = relationship("Unit",backref="owner")


    def __repr__(self):
        return self.name


class Unit(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(512), nullable=False)

    def __repr__(self):
        return self.name