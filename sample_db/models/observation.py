from geoalchemy2 import Geometry
from lccs_db.models import BaseModel
from sqlalchemy import Column, Date, ForeignKey, Integer


class Observation(BaseModel):
    __tablename__ = 'observation'

    id = Column(Integer, primary_key=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    location = Column(Geometry(geometry_type='POINT', srid=4326))
    class_id = Column(Integer, ForeignKey('luc_class.id', ondelete='NO ACTION'), nullable=False)