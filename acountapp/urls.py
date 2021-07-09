from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from acountapp.views import mainView, AccountCreateView, AccountLoginView

app_name = 'accountapp'

urlpatterns = [
    path('main/', mainView, name='main_view'),

    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create_user'),

]