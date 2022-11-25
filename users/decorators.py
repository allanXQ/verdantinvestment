from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated(view):
    def wrapper(request, *args, **kwargs):
        if (request.user.is_authenticated):
            return redirect('dashboard')
        else:
            return view(request, *args, **kwargs)
    return wrapper
