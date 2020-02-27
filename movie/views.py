import json
import logging

from django.forms import model_to_dict
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST

from basic.commonUtils import LocalCacheUtil
from basic.httpUtils import ResponseHelper
from movie import constants
from movie.services import FilmService
logger = logging.getLogger('log')

@require_http_methods(["POST"])  # require_POST()
def support_film(request):
    """
    Give a like to film
    :return:
    """
    film_id = request.POST.get('film_id')
    if film_id is None :
        return ResponseHelper.build_fail(constants.FILM_ID_IS_EMPTY)

    film_service = FilmService()
    film_service.support_film(film_id)
    return ResponseHelper.build_success(None)


@require_POST
def get_films(request, start=1, amount=5):
    """
    Get the films
    :param request:
    :param start:
    :param amount:
    :return:
    """
    pass


class FilmView(View):

    def get(self, request):
        film_id = request.GET.get('film_id')
        logger.debug("film_id:{}".format(film_id))
        if film_id is None:
            return ResponseHelper.build_fail("film_id is empty")
        film_service = FilmService()
        film = film_service.get_film_by_id(film_id)
        return ResponseHelper.build_success(model_to_dict(film))

    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        img = data.get('img')
        video = data.get('video')
        main_page = data.get('main_page')
        if name is None:
            return ResponseHelper.build_fail("name is empty")
        film_service = FilmService()
        film_id = film_service.create_film(name, img, video, main_page);
        return ResponseHelper.build_success({"film_id": film_id})

    @csrf_exempt
    def put(self, request):
        data = json.loads(request.body)
        film_id = data.get('film_id')
        img = data.get('img')
        video = data.get('video')
        main_page = data.get('main_page')
        if film_id is None:
            return ResponseHelper.build_fail(constants.FILM_ID_IS_EMPTY)

        if img is None and video is None and main_page is None:
            return ResponseHelper.build_fail(constants.UPDATED_FIELDS_ARE_EMPTY)

        film_service = FilmService()
        film_service.update_film_by_id(film_id,img,video,main_page)
        return ResponseHelper.build_success()



    def delete(self, request):
        # Check whether the user login
        token = request.META.get("TOKEN")
        if token is None:
            return ResponseHelper.build_fail('Please login first')
        user_dict = LocalCacheUtil.get_data("token-" + token.__str__())
        if user_dict is not None:
            return ResponseHelper.build_fail('Please login first')
        film_id = request.GET.get("film_id")
        if film_id is None :
            return ResponseHelper.build_fail('Please choose the film to delete')
        logger.debug('begin to delete film , film id is :{}'.format(film_id))

        film_service = FilmService();
        film_service.delete_movie(film_id)
        return ResponseHelper.build_success()
