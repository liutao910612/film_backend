from movie.models import Film


class MovieService:

    def create_movie(self, name, img, video, main_page):
        """
        create movie
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

    def update_movie_by_id(self, id, img, video, main_page):
        """
        update movie
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
        film = Film.objects.filter(id=id).get()
        if img is not None:
            film.img = img

        if video is not None:
            film.video = video

        if main_page is not None:
            film.main_page = main_page

        film.save()

