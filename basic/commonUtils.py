import re

from django.core.cache import cache


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


class LocalCacheUtil:

    @staticmethod
    def add_cache(key, value, time_out):
        cache.set(key, value, time_out)

    @staticmethod
    def get_cache(key):
        return cache.get(key)

    @staticmethod
    def delete_cache(key):
        cache.delete(key)


    @staticmethod
    def clear_all():
        cache.clear()

    @staticmethod
    def touch_cache(key,time_out):
        """
        Update the expired time of key
        :param key:
        :param time_out:
        :return:
        """
        return cache.touch(key,time_out)

    @staticmethod
    def incr(key,delta = 1):
        if delta <= 0:
            raise Exception("delta must be bigger than zero")
        return cache.incr(key,delta)

    @staticmethod
    def decr(key,delta = 1):
        if delta <= 0:
            raise Exception("delta must be bigger than zero")
        return cache.decr(key,delta)

