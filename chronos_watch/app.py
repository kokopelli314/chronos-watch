import falcon
import os, pathlib, sys
from peewee import SqliteDatabase
# from models import punch
from .models.punch import Punch


database = SqliteDatabase('punches.db')

# Connection to database
class PeeweeConnectionMiddleware(object):
    def process_request(self, req, resp):
        database.connect()

    def process_response(self, req, resp, resource):
        if not database.is_closed():
            database.close()


"""Time punch, in or out."""
class PunchResource(object):
    def on_post(self, req, resp):
        print('hello -- we got a post!', file=sys.stderr)
        print(req.context)
        pass

    def on_get(self, req, resp):
        """Get list of punches."""
        resp.status = falcon.HTTP_200
        resp.body = 'List of punches :)'


app = application = falcon.API(middleware=[
    PeeweeConnectionMiddleware()
])

STATIC_PATH = pathlib.Path(__file__).parent / 'client'

app.add_static_route('/', str(STATIC_PATH))
app.add_route('/api/punch', PunchResource())

