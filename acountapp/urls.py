from django.urls import path

from acountapp.views import mainView


app_name = 'accountapp'

urlpatterns = [
    path('hello/', mainView, name='main_view'),

]