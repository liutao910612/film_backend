import hashlib
import random

from django.db import connection

from account.models import User
from basic.utils import CommonUtils


class UserService:
    ALPHABET = "zyxwvutsrqponmlkjihgfedcba"
    """
    I will use raw sql for this service
    """
    def register_user(self,first_name, last_name, password, email, phone,address,hobby):

        # Check whether the phone exist
        count = User.objects.filter(phone=phone).count()
        if count > 0:
            return 0

        salt = "".join(random.sample(self.ALPHABET,5))
        md5 = hashlib.md5(salt)
        md5.update(password.encode('utf-8'))
        pwd = md5.hexdigest()
        user_id = self.create_user(first_name,last_name,pwd,email,phone)
        self.create_user_detail(user_id,address,hobby)
        return 1

    def create_user(self,first_name, last_name, password, email, phone):

        return 1

    def create_user_detail(user_id, address, hobby):
        pass

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
            cursor.execute(sql,[user_id])
            dict = CommonUtils.dictfetchall(cursor)
        return dict
