from django.urls import path

from acountapp.views import mainView


app_name = 'accountapp'

urlpatterns = [
    path('main/', mainView, name='main_view'),

]