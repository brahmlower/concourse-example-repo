
import json
import falcon

from . import data_access

class BaseHandler(object):
    def __init__(self, config, db):
        self.config = config
        self.db = db

    def _to_json(self, result_proxy):
        return json.dumps([(dict(row.items())) for row in result_proxy])

class RootHandler(BaseHandler):
    def on_get(self, req, resp):
        resp.body = json.dumps({'message': 'Hello world!'})
        resp.status = falcon.HTTP_200
        resp.content_type= 'application/json'
        return resp

class BuildingHandler(BaseHandler):
    def on_get(self, req, resp, building_id):
        result = data_access.db_buildings_get(self.db, building_id)
        # Construct response
        resp.status = falcon.HTTP_200
        resp.body = self._to_json(result)
        resp.content_type= 'application/json'
        return resp

class BuildingListHandler(BaseHandler):
    def on_get(self, req, resp):
        result = data_access.db_buildings_all(self.db)
        # Construct response
        resp.status = falcon.HTTP_200
        resp.body = self._to_json(result)
        resp.content_type= 'application/json'
        return resp
