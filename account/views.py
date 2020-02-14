import json

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

    @csrf_exempt()
    def post(self, request):
        """
        Register user
        :param request:
        :return:
        """
        data = json.loads(request.body)
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        phone = data.get("phone")
        email = data.get("email")
        password = data.get("password")
        address = data.get("address")
        hobby = data.get("hobby")

        if first_name is None or len(first_name) > 10 or len(first_name) < 1:
            return ResponseHelper.build_fail(constants.FIRST_NAME_IS_INVALID)

        if last_name is None or len(last_name) > 10 or len(last_name) < 1:
            return ResponseHelper.build_fail(constants.LAST_NAME_IS_INVALID)

        if phone is None or len(phone) > 10 or len(phone) < 6:
            return ResponseHelper.build_fail(constants.PASSWORD_IS_INVALID)


        pass

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
        pass
