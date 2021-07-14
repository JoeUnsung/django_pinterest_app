from django.urls import path

from profile_app.views import ProfileCreateView


app_name = 'profile_app'

urlpatterns = [
    path('make/', ProfileCreateView.as_view(), name='make_profile'),


]
