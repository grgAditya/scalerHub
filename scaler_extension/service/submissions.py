import base64

class SubmissionsService:

    def __init__(self):
        pass

    def submit_solution(self, programming_language_id, class_id, question_id, code_submission):
        """
        submission
        :return:
        """
        github_folder_name = str(class_id) + "_" + str(question_id)
        code_submission_base64 = base64.decodebytes(s=code_submission)
        code_submission_string = code_submission_base64.decode("utf-8")
        print(code_submission_string)



if __name__ == "__main__":
    code_b64 = base64.encodebytes(b"print(1243543)")
    SubmissionsService().submit_solution(programming_language_id=11, class_id='1234', question_id='6345',
                                         code_submission=code_b64)

