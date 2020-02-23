import json

from django.db import transaction
from django.forms import model_to_dict
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from account import constants
from account.exceptions import RegisterException
from account.services import UserService, EmailCodeService, SessionService
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
        try:
            count = user_service.register_user(email,email_code,password)
        except RegisterException as e:
            return ResponseHelper.build_fail(e.reason)
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

    def get(self,request):
        """
        Get email code
        :param email:
        :param is_test:
        :return:
        """
        email = request.GET.get("email")
        is_test = request.GET.get("is_test")
        email_code_service = EmailCodeService()
        email_code = email_code_service.send_email(email,is_test)
        if is_test:
            return ResponseHelper.build_success({"email_code":email_code})

        return ResponseHelper.build_success()

# session manager
class SessionView(View):

    @csrf_exempt
    def post(self, request):
        """
        login
        :param request:
        :return:
        """
        data = json.loads(request.body)
        email = data['email']
        password = data['password']

        # check parameter
        if email is None or len(email) == 0:
            return ResponseHelper.build_fail(constants.EMAIL_IS_INVALID)
        if password is None or len(password) == 0:
            return ResponseHelper.build_fail(constants.PASSWORD_IS_INVALID)

        session_service = SessionService()
        token = session_service.create_session(email,password)
        return ResponseHelper.build_success({"token":token.__str__()})

    # User login out
    def delete(self, request):
        token = request.META.get("TOKEN")
        if token is None:
            return ResponseHelper.build_fail('token is null')
        username = SessionService.delete_session(token)
        return  ResponseHelper.build_success({"username":username})

