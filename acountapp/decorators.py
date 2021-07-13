from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def decorator(func):
    def decorated(request, *args, **kwargs):
        user_pk = User.objects.get(pk=kwargs['pk'])
        if not request.user == user_pk:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated