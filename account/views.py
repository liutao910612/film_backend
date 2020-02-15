import json

from django.db import transaction
from django.forms import model_to_dict
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from account import constants
from account.services import UserService
from basic.httpUtils import ResponseHelper


class UserView(View):

    def get(self, request):
        """
        Get user including detail information
        :param request:
        :return:
        """
        token = request.META.get("TOKEN")
        # TODO get user_id by token
        user_id = 1
        user_service = UserService()
        user_detail = user_service.get_user_detail_by_id(user_id)
        return ResponseHelper.build_success(model_to_dict(user_detail))

    @csrf_exempt
    @transaction.atomic
    def post(self, request):
        """
        Register user
        :param request:
        :return:
        """
        data = json.loads(request.body)
        email = data.get("email")
        email_code = data.get("email_code")
        password = data.get("password")

        user_service = UserService()
        count = user_service.register_user(email,email_code,password)
        if count < 1:
            return ResponseHelper.build_fail(constants.REGISTER_FAIL)

        return ResponseHelper.build_fail(constants.REGISTER_SUCCESS)

    def put(self, request):
        """
        Update user
        :param request:
        :return:
        """
        pass

    def delete(self, request):
        """
        Delete user
        :param request:
        :return:
        """
        token = request.META.get("TOKEN")
        # TODO get user_id by token
        user_id = 1
        user_service = UserService()
        user_service.delete_user(user_id)

        # TODO logout user
        return ResponseHelper.build_success()

class EmailCodeView(View):
    def get(self,email):
        pass
