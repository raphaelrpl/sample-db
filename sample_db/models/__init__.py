"""SampleDB Models package"""


from lccs_db.models.base import db, BaseModel
from .observation import Observation


__all__ = ('db', 'Observation', 'BaseModel', )
