from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from acountapp.views import mainView, accountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('main/', mainView, name='main_view'),

    path('login/', LoginView.as_view(template_name='acountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', accountCreateView.as_view(), name='create_user'),

]