from django.test import TestCase
from movie.models import Film, Blog


class UserModelTest(TestCase):
    def testSaveData(self):
        # film = Film('呼啸山庄', 'https://www.baidu.com/', 'https://www.baidu.com/', 0, 0, None)
        film = Film.objects.all().filter(name="呼啸山庄")
        print(film)