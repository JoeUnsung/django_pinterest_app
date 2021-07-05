from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from acountapp.models import Content
# Create your views here.


def mainView(request):
    if request.method == "GET":
        result = Content.objects.all()
        return render(request, 'acountapp/main.html', context={'res': {'output': result}})

    if request.method == "POST":
        id = request.POST.get('id')

        cont = Content()
        cont.id = id
        cont.text = 'test body'
        cont.save()

        result = Content.objects.all()
        return HttpResponseRedirect(reverse('accountapp:main_view'))
        # return render(request, 'acountapp/main.html', context={'res': {'output':  result}})
