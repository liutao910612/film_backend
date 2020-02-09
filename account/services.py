from account.models import User


class UserService:
    """
    I will use raw sql for this service
    """

    def create_user(first_name, last_name, password, email, phone, is_admin):
        pass

    def create_user_detail(user_id, address, hobby):
        pass

    def delete_user(self, user_id):
        pass

    def get_user_by_phone(self, phone):
        """
        get user by phone
        :param phone:
        :return:
        """
        sql = 'select id first_name' \
              ',last_name' \
              ',password' \
              ',email' \
              ',phone' \
              ',is_admin ' \
              'from account_user ' \
              'where phone = %s'
        user = User.objects.raw(sql,[phone])[0];
        return user


