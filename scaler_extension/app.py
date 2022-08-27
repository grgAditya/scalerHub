from wsgiref import simple_server

import falcon

from scaler_extension.resources.submissions import SubmissionsResource
from scaler_extension.resources.users import UserResource


app = falcon.App(middleware=[])

app.add_route('/submissions', SubmissionsResource())
app.add_route('/users', UserResource())

if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8001, app)
    httpd.serve_forever()
