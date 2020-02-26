from typing import Callable
from geoalchemy2 import Geometry
from lccs_db.models import BaseModel, LucClass, db
from sqlalchemy import Column, Date, ForeignKey, Integer, Table


def make_observation(table_name: str, create: bool = False) -> Callable[Table]:
    """Create customized observation model using a table name.

    TODO: Create an example

    Args:
        table_name - Table name
        create - Flag to create if not exists

    Returns
        Observation definition
    """
    klass = Table('{}_observations'.format(table_name), BaseModel.metadata,
        Column('user_id', Integer, primary_key=True),
        Column(
            'class_id',
            Integer,
            ForeignKey(LucClass.id, ondelete='NO ACTION', onupdate='CASCADE'),
            nullable=False
        ),
        Column('start_date', Date, nullable=False),
        Column('end_date', Date, nullable=False),
        Column('location', Geometry(srid=4326))
    )

    if create:
        if not db.engine.dialect.has_table(db.engine, klass.name):
            BaseModel.metadata.tables[klass.name].create(bind=db.engine)

    return klass
