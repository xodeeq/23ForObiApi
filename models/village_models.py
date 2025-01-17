import datetime
from uuid import uuid4

import bigfastapi.db.database as db
from bigfastapi.models.location_models import Location
from bigfastapi.models.user_models import User
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from sqlalchemy.types import String


class StateDetails(db.Base):
    __tablename__ = "state_details"
    id = Column(String(255), primary_key=True, index=True, default=uuid4().hex)
    state_code = Column(String(2), nullable=False)
    current_governor = Column(String(50), nullable=True)
    state_capital = Column(String(50), nullable=True)


class Village(db.Base):
    __tablename__ = "villages"
    id = Column(String(255), primary_key=True, index=True, default=uuid4().hex)
    name = Column(String(255), index=True)
    location = Column(String(255), ForeignKey(Location.id))
    contributed_by = Column(String(255), ForeignKey(User.id))

    voters = relationship("Voter", back_populates="village")


class UserVillage(db.Base):
    __tablename__ = "user_villages"
    id = Column(String(255), primary_key=True, index=True, default=uuid4().hex)
    village = Column(String(255), ForeignKey(Village.id))
    user = Column(String(255), ForeignKey(User.id))
