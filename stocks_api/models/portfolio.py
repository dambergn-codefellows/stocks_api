from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import(
  Column,
  Index,
  integer,
  Text,
  DateTime,
)

class StocksLocation(Base):
  __tablename__ = 'locations'
  id = Column(Integer, primary_key=True)
  name = Column(Text)
  zip_code = Column(Integer, unique=True)

  date_created = Column(DateTime, default=dt.now())
  date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

  @classmethod
  def new(cls, request=None, **kwargs):
    if request.dbsession is None:
      raise DBAPIError

      weather = cls(**kwargs)
      request.dbsession.add(weather)

      return request.dbsession.query(cls).filter(
        cls.zip_code == kwargs['zip_code']).one_or_none()


  @classmethod
  def all(cls, request=None):
    if request.dbsession is None:
      raise DBAPIError

      return request.dbsession.query(cls).all()

  @classmethod
  def one(cls, request=None, pk=None):
    if request.dbsession is None:
      raise DBAPIError

      return request.dbsession.query(cls).get(pk)

  @classmethod
  def remove(cls, request=None, pk=None):
    if request.dbsession is None:
      raise DBAPIError

    return request.dbsession.query(cls).get(pk).delete()