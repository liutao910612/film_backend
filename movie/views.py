import json

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST

from basic.httpUtils import ResponseHelper
from movie import constants
from movie.services import FilmService


@require_http_methods(["POST"])  # require_POST()
def support_film(request):
    """
    Give a like to film
    :return:
    """
    film_id = request.GET.get('film_id')
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
        if film_id is None:
            return ResponseHelper.build_fail("film_id is empty")
        film_service = FilmService()
        film = film_service.get_film_by_id(film_id)
        return ResponseHelper.build_success(model_to_dict(film))

    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)
        name = data['name']
        img = data['img']
        video = data['video']
        main_page = data['main_page']
        if name is None:
            return ResponseHelper.build_fail("name is empty")
        film_service = FilmService()
        film_id = film_service.create_film(name, img, video, main_page);
        return ResponseHelper.build_success({"film_id": film_id})

    @csrf_exempt
    def put(self, request):
        data = json.loads(request.body)
        film_id = data['film_id']
        img = data['img']
        video = data['video']
        main_page = data['main_page']
        if film_id is None:
            return ResponseHelper.build_fail(constants.FILM_ID_IS_EMPTY)

        if img is None and video is None and main_page is None:
            return ResponseHelper.build_fail(constants.UPDATED_FIELDS_ARE_EMPTY)

        film_service = FilmService()
        film_service.update_film_by_id(film_id,img,video,main_page)
        return ResponseHelper.build_success()



    def delete(self, request):
        pass
