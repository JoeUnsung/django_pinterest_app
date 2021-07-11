from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.models import User

from acountapp.forms import AccountUpdateForm
from acountapp.models import Content
# Create your views here.


def mainView(request):
    if request.method == "GET":
        result = Content.objects.all()
        result2 = User.objects.all()
        # return render(request, 'acountapp/main.html', context={'res': {'output': result}})
        return render(request, 'acountapp/main.html', context={'res': {'output': result2}})

    if request.method == "POST":
        id = request.POST.get('id')

        cont = Content()
        cont.id = id
        cont.text = 'test body'
        cont.save()

        result = Content.objects.all()
        return HttpResponseRedirect(reverse('accountapp:main_view'))
        # return render(request, 'acountapp/main.html', context={'res': {'output':  result}})

class AccountCreateView(CreateView): # Create 뷰
    model = User
    form_class = UserCreationForm
    template_name = 'acountapp/create_user.html'
    success_url = reverse_lazy('accountapp:main_view')

class AccountLoginView(LoginView):
    template_name = 'acountapp/login.html'

class AccountProfileView(DetailView): # Read 뷰
    model = User
    context_object_name = 'login_user'
    template_name = 'acountapp/profile.html'

class AccountUpdateView(UpdateView): #Update 뷰
    model = User
    form_class = AccountUpdateForm
    template_name = 'acountapp/update_user.html'
    success_url = reverse_lazy('accountapp:main_view')

