
import os
import sys
import yaml

import falcon
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

from .handlers import RootHandler
from .handlers import BuildingHandler
from .handlers import BuildingListHandler

def _load_config(cfg_path):
    print("Reading settings from file: {}".format(cfg_path))
    try:
        with open(cfg_path, 'r') as stream:
            try:
                return (True, yaml.load(stream))
            except yaml.YAMLError as exc:
                return (False, exc)
    except FileNotFoundError:
        message = "No such file or directory: '{}'".format(cfg_path)
        return (False, message)
    except:
        message = "General error while opening config file: '{}'".format(cfg_path)
        return (False, message)

def _load_db(db_config):
    url = "postgresql://{username}:{password}@{hostname}:{port}/{database}".format(**db_config)
    engine = create_engine(url, poolclass = NullPool)
    return engine

def app(settings_path="./settings.yml"):
    # Read the config file
    (cfg_success, cfg_result) = _load_config(settings_path)
    if cfg_success is False:
        sys.exit(cfg_result)
    app_config = cfg_result
    print(app_config)
    # Initialize the database
    db_conn = _load_db(app_config['db'])
    # Build the app object
    app = falcon.API()
    app.add_route('/', RootHandler(app_config, db_conn))
    app.add_route('/buildings', BuildingListHandler(app_config, db_conn))
    app.add_route('/buildings/{building_id}', BuildingHandler(app_config, db_conn))
    return app
