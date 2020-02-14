import re


class RegUtils:

    @staticmethod
    def check_email(email):
        """
        check whether the email is invalid
        :param email:
        :return:
        """
        ex_email = re.compile(r'^[1-9][0-9]{4,10}@qq\.com')
        return ex_email.match(email)

    @staticmethod
    def check_phone(phone):
        """
        Check whether the phone is invalid
        :param phone:
        :return:
        """
        ex_phone = re.compile(r'^[1][2-9]\\d{9}')
        return ex_phone.match(phone)
