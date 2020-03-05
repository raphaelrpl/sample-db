import os
import subprocess

import click
import sqlalchemy
from lccs_db.cli import create_cli, create_app, create_db as lccs_init_db
# from lccs_db.cli import Config, init_db as lccs_init_db, create_tables as lccs_create_tables, pass_config
from sqlalchemy import text
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import create_database, database_exists


cli = create_cli(create_app=create_app)





# @click.group()
# @click.option('--user', type=click.STRING, default='postgres', help='PostgreSQL user.')
# @click.option('--host', type=click.STRING, default='localhost', help='PostgreSQL host.')
# @click.option('--password', prompt=True, hide_input=True, default=None, help='PostgreSQL password.')
# @click.option('--port', type=click.INT, default=5432, help='PostgreSQL port.')
# @click.option('--db_name', type=click.STRING, default=None, help='PostgreSQL database name.')
# @pass_config
# def cli(config, user, host, password, port, db_name):
#     """Sample db command line utility."""
#     config.uri = "postgresql://{}:{}@{}:{}/{}".format(user, password, host, port, db_name)

#     config.engine = sqlalchemy.create_engine(config.uri)

#     Session = scoped_session(sessionmaker(bind=config.engine))

#     config.session = Session()


@cli.command()
@click.pass_context
# @pass_config
def init_db(ctx: click.Context):
    from lccs_db.models import db as _db
    """Initial Database."""
    ctx.forward(lccs_init_db)

    click.secho('Creating schema sample_db...', fg='green')

    _db.session.execute("CREATE EXTENSION IF NOT EXISTS postgis")
    _db.session.execute("CREATE SCHEMA IF NOT EXISTS sample_db")
    _db.session.commit()


# @cli.command()
# @click.pass_context
# @pass_config
# def create_tables(config: Config, ctx: click.Context):
#     """Initial Database."""
#     ctx.forward(lccs_create_tables)

#     env = os.environ.copy()
#     env["PYTHONPATH"] = "."
#     env["PATH"] = "{}:{}".format(os.path.expanduser("~/.local/bin"), env["PATH"])
#     env["SQLALCHEMY_DATABASE_URI"] = config.uri

#     sp = subprocess.Popen(["alembic", "upgrade", "head"], env=env)

#     if (sp.wait() != 0):
#         raise ValueError("Alembic upgrade head error ")
