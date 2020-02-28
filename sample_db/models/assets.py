from typing import Callable
from geoalchemy2 import Geometry
from lccs_db.models import LucClass, db
from sqlalchemy import Column, ForeignKey, Integer, String, Table

from .base import metadata


def make_assets(table_name: str, observation: Table, create: bool = False) -> Table:
    """Create customized assets model using a table name.

    TODO: Create an example

    Args:
        table_name - Table name
        observation - SQLALchemy Table Observation
        create - Flag to create if not exists

    Returns
        Observation definition
    """

    klass = Table('{}_assets'.format(table_name), metadata,
        Column('id', Integer, primary_key=True),
        Column(
            'observation_id',
            Integer,
            ForeignKey(observation.id, ondelete='NO ACTION', onupdate='CASCADE'),
            nullable=False
        ),
        Column('url', String, nullable=False),
    )

    if create:
        if not klass.exists(bind=db.engine):
            klass.create(bind=db.engine)

    return klass
