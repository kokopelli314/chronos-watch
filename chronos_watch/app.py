import falcon
import os, pathlib, sys
from peewee import SqliteDatabase
from playhouse.shortcuts import model_to_dict
# from models import punch
from chronos_watch.models.punch import Punch


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
        print('Post received!', file=sys.stderr)
        body = req.media
        try:
            punch = Punch(
                timestamp=body['timestamp'],
                punch_type=body['punch_type']
            )
            punch.save()
        except KeyError:
            print('Missing key!')


    def on_get(self, req, resp):
        """Get list of punches."""
        resp.status = falcon.HTTP_200
        punches = Punch.select()
        json_list = list(map(model_to_dict, punches))
        resp.media = {
            'punches': json_list
        }


app = application = falcon.API(middleware=[
    PeeweeConnectionMiddleware()
])

STATIC_PATH = pathlib.Path(__file__).parent / 'client'

app.add_static_route('/', str(STATIC_PATH))
app.add_route('/api/punch', PunchResource())

if __name__ == '__main__':
    from waitress import serve
    database.create_tables([Punch])
    serve(app, listen='*:8000')
