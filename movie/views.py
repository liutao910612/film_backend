from django.http import HttpResponse
from django.views import View
from django.views.decorators.http import require_http_methods, require_POST


@require_http_methods(["POST"])  # require_POST()
def support_film(request):
    """
    Give a like to film
    :return:
    """

    # Any view should return httpResponse object
    return HttpResponse('ok')


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
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
