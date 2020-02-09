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

    def get_film_by_name(self, name):
        """
        get films liking name
        :param name: 
        :return: 
        """
        films = Film.objects.get(name__icontains=name)
        return films

    def delete_movie(self, id):
        """
        delete movie by logic
        :param id:
        :return:
        """
        film = Film.objects.get(id=id)
        film.is_deleted = 1
        return film