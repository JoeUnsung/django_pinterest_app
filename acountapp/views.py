from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def mainView(request):
    if request.method == "GET":
        return render(request, 'acountapp/main.html')

    if request.method == "POST":

        request = request
        return render(request, 'acountapp/main.html', context={'text': {'name': 'DJANGO', 'content': 'LETS BREAK DJANGO'}})
