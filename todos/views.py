from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
@ensure_csrf_cookie
@never_cache
def home(request):
    return render(request, 'root.html', {})
