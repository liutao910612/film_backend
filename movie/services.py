from django.db.models import Q, F, Avg, Max, Min

from movie.models import Film


class MovieService:

    def create_film(self, name, img, video, main_page):
        """
        create film
        :param name:
        :param img:
        :param video:
        :param main_page:
        :return:
        """

        """
        create a object and save it , like follow:
        film = Film(name=name, img=img, video=video, main_page=main_page)
        film.save()
        """
        film = Film.objects.create(name=name, img=img, video=video, main_page=main_page)
        return film.id

    def delete_movie(self, id):
        """
        delete movie by logic
        :param id:
        :return:
        """
        film = Film.objects.get(id=id)
        film.is_deleted = 1
        film.save()

        """
        we can use update() to update more data , not only one.like follow:
        Film.objects.filter(update_time = date(2019, 5, 6)).update(suppose_num=0)
        """
        return film

    def get_film_by_id(self, id):
        """
        get film by id
        you can get the object by using get()
        the parameters of get() like filter(), but , the result of filter() is QuerySet
        :param id:
        :return:
        """

        film = Film.objects.get(id=id)
        return film

    def get_film_by_str(self, str):
        """
        get films liking str
        If you want to more complex query, you can use Q object.
        :param str:
        :return:
        """
        films = Film.objects \
            .order_by('name') \
            .get(Q(name__icontains=str) | Q(desc__icontains=str))
        return films

    def update_film_by_id(self, id, img, video, main_page):
        """
        update film
        :param id:
        :param img:
        :param video:
        :param main_page:
        :return:
        """

        """
        要从数据库检索对象，需要通过模型类的Manager构架你一个QuerySet
        一个 QuerySet 代表来自数据库中对象的一个集合
        """
        film = Film.objects.get(id=id)
        if img is not None:
            film.img = img

        if video is not None:
            film.video = video

        if main_page is not None:
            film.main_page = main_page

        film.save()

    def support_film(self, id):
        """
        give a like to film
        :param id:
        :return:
        """
        Film.objects.filter(id=id).update(suppose_num=F('suppose_num') + 1)

    def get_download_num_info(self):
        return Film.objects.aggregate(avg=Avg('download_num')
                                      , max=Max('download_num')
                                      , min=Min('download_num'))
