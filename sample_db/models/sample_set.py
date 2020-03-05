from lccs_db.models.base import BaseModel
from lccs_db.models import LucClassificationSystem
from geoalchemy2 import Geometry
from sqlalchemy import Column,ForeignKey, Integer, String, Text


class SampleSet(BaseModel):
    __tablename__ = 'sample_set'
    __table_args__ = dict(schema='sample_db')

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    groups = Column(String, nullable=True)
    oauth = Column(String, nullable=True)
    luc_classification_system_id = Column(Integer, ForeignKey(LucClassificationSystem.id, onupdate='CASCADE', ondelete='NO ACTION'), nullable=False)