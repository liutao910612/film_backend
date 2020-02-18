import hashlib
import math
import random

from django.db import connection

from account.models import User, UserDetail
from basic.utils import CommonUtils, EmailUtils


class UserService:
    ALPHABET = "zyxwvutsrqponmlkjihgfedcba"
    """
    I will use raw sql for this service
    """

    def register_user(self, email, email_code, password):
        # Check email
        count = User.objects.filter(email=email).count()
        if count > 0:
            return 0

        # TODO Check email code

        salt = "".join(random.sample(self.ALPHABET, 5))
        md5 = hashlib.md5(salt)
        md5.update(password.encode('utf-8'))
        pwd = md5.hexdigest()
        user = User(email=email, password=pwd, salt=salt)
        user.save()
        return 1

    def create_user(self, first_name, last_name, password, email, phone, salt):
        """
        Create user
        :param first_name:
        :param last_name:
        :param password:
        :param email:
        :param phone:
        :param salt:
        :return:
        """
        user = User(first_name, last_name, password, email, phone, salt)
        user.save()

    def create_user_detail(self, user_id, address, hobby):
        """
        Create user detail
        :param user_id:
        :param address:
        :param hobby:
        :return:
        """
        userDetail = UserDetail(user_id, address, hobby)
        userDetail.save()

    def delete_user(self, user_id):
        """
        delete user by sql
        :param user_id:
        :return:
        """
        sql = 'update account_user set is_deleted = 1 where id = %s'
        with connection.cursor() as cursor:
            cursor.execute(sql, [user_id])
            row = cursor.fetchone()

        return row

    def get_user_by_phone(self, phone):
        """
        get user by phone
        :param phone:
        :return:
        """
        sql = 'select id ,first_name' \
              ',last_name' \
              ',password' \
              ',phone ' \
              'from account_user ' \
              'where phone = %s'
        user = User.objects.raw(sql, [phone])[0];
        return user

    def get_user_detail_by_id(self, user_id):
        """
        return dictionary ,not list
        :param user_id:
        :return:
        """
        sql = 'select a.id' \
              ',a.first_name' \
              ',a.last_name' \
              ',a.phone' \
              ',b.address' \
              ',b.hobby from account_user a inner join account_userdetail b on a.id = b.user_id ' \
              ' where a.id = %s'
        with connection.cursor() as cursor:
            cursor.execute(sql, [user_id])
            dict = CommonUtils.dictfetchall(cursor)
        return dict


class EmailCodeService:
    ALPHABET = "zyxwvutsrqponmlkjihgfedcba"

    def send_email(self, email, is_test):
        email_code = self.__get_email_code()
        if is_test == 1:
            return email_code

        subject = "Register Email Code"
        message = "you email code is : " + email_code
        from_email = "film.backend@alvin.com"
        to_email = email
        EmailUtils.send_email(subject,message,from_email,to_email)

    def __get_email_code(self):
        """
        Get email code
        :return:
        """
        email_code = ""
        for i in range(6):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            email_code += ch
        return email_code
