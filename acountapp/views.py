from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView
from django.contrib.auth.models import User

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


class accountCreateView(CreateView):
    model = User
    fields = [
        'username',
        'password',
        'email',
        'first_name',
        'last_name',
    ]
    form = UserCreationForm
    template_name = 'acountapp/create_user.html'
    success_url = reverse_lazy('accountapp:main_view')
