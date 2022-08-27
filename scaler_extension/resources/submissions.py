from scaler_extension.service.submissions import SubmissionsService
import falcon

class SubmissionsResource:

    def on_get(self, req, resp):
        """

        :param req: request received to endpoint
        :param resp: response object to be sent
        :return:
        """
        resp.body = {"status": "success_hello"}
        resp.status = falcon.HTTP_200
        return resp


    def on_post(self, req, resp):

        """

        :param req:
        {
            "programming_language_id": 11,
            "class_id" : 54362,
            "question_id": 123,
            "code_submission" : "print(test123); "
        }

        :param resp:
        :return:
        """
        try:
            request_body = req.body
            submission_service = SubmissionsService()
            submission_service.submit_solution(**request_body)
        except Exception as e:
            raise e
        pass

    def on_put(self, req, resp):
        pass
