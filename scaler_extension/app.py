import falcon

from scaler_extension.resources.submissions import SubmissionsResource
from scaler_extension.resources.users import UserResource


app = falcon.App(middleware=[])

app.add_route('/submissions', SubmissionsResource())
app.add_route('/users', UserResource())

