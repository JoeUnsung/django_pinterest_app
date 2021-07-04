from django.urls import path

from acountapp.views import hello_django


app_name = 'acountapp'

urlpatterns = [
    path('hello/', hello_django, name='hello_django'),

]