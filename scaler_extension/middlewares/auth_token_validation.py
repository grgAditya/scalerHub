class AuthTokenValidator:

    def __init__(self):
        pass

    def req_needs_auth(self, req):
        exclude_paths = [""]
        if req.path in exclude_paths:
            return False
        return True


    def process_request(self, req, resp):
        """

        :param req:
        :param resp:
        :return:
        """
        if not self.req_needs_auth(req):
            return

        self.github_auth_validation()





