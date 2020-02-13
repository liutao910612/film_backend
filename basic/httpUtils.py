from django.forms import model_to_dict
from django.http import JsonResponse


class ResponseEntity:
    code = 0
    msg = ''
    data = None

    def __init__(self, code, msg, data):
        self.code = code
        self.msg = msg
        self.data = data


class ResponseHelper:

    @classmethod
    def build_success(self, data=None):
        if data is None:
            return JsonResponse(ResponseEntity(1, None, None).__dict__)
        return JsonResponse(ResponseEntity(1, None, data).__dict__)

    @classmethod
    def build_fail(self, msg=None):
        return JsonResponse(ResponseEntity(0, msg, None).__dict__)
