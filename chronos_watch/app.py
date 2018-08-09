import falcon
import os, pathlib

"""Time punch, in or out."""
class PunchResource(object):
    def on_post(self):
        pass

    def on_get(self, req, resp):
        """Get list of punches."""
        resp.status = falcon.HTTP_200
        resp.body = 'List of punches :)'


app = application = falcon.API()

STATIC_PATH = pathlib.Path(__file__).parent / 'client'

app.add_static_route('/', str(STATIC_PATH))
app.add_route('/api/punch', PunchResource())

