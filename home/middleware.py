from django.shortcuts import redirect
from django.conf import settings

from django.shortcuts import redirect
from django.urls import resolve



class InvalidURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Resuelve la URL solicitada
        resolver = resolve(request.path_info)
        if not resolver.url_name:
            # La URL no es válida, redirige a la página de inicio
            return redirect('home_page')

        response = self.get_response(request)
        return response
