from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profile_app.models import Profile
from profile_app.forms import ProfileCreationForm

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'login_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:main_view')
    template_name = 'profile_app/create_profile.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False) # commit을 False로 설정함으로써 실제 DB 저장을 잠시 이연
        temp_profile.user = self.request.user # 요청을 보낸 user의 정보를 저장하면서 profile내 객체에 user정보를 포함

        temp_profile.save() # DB 저장
        return super().form_valid(form) #기존의 함수를 그대로 반환