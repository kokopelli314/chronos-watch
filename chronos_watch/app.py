import falcon
import os

# Main view route
class ViewResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        filename = os.path.abspath('chronos_watch/client/index.html')
        resp.stream = open(filename, 'rb')

api = app = application = falcon.API()
# api.add_route('/', ViewResource())
import pathlib
STATIC_PATH = pathlib.Path(__file__).parent / 'client'
# print(os.path.abspath('chronos_watch/client/index.html'))
# print('test')
# print(STATIC_PATH)
api.add_static_route('/', str(STATIC_PATH))
