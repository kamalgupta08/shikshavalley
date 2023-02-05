class ResponseHelper:
    def __int__(self):
        print()
        pass

    def get_success_response(self, message="", data=None):
        response = {
            "status": True,
        }
        if data:
            response["data"] = data
        if message:
            response["success_message"] = message
        return response

    def get_error_response(self, message="", error_data=None, error_code=""):
        response = {
            "status": False,
            "error_message": message
        }

        if error_code:
            response["error_code"] = error_code

        if error_data:
            response["error_data"] = error_data

        return response