from django.urls import path

from acountapp.views import mainView, accountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('main/', mainView, name='main_view'),

    path('create/', accountCreateView.as_view(), name='create_user'),

]