from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect


# @@@@@ DECORADORES @@@@@ #

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('perfil')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def user_type_required(user_types=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user.user_type in user_types:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(
                    request, 'Você não tem permissão para acessar esta página.')
                return redirect('login')
        return wrapper
    return decorator



