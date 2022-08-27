import falcon

from scaler_extension.resources.submissions import SubmissionsResource

app = falcon.App()
app.add_route('/quote', SubmissionsResource())

