import falcon
import os

# Main view route
class ViewResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        filename = os.path.abspath('chronos_watch\client\index.html')
        resp.stream = open(filename, 'rb')

app = application = falcon.API()
app.add_route('/', ViewResource())
