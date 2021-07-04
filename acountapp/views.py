from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello_django(request):

    # return HttpResponse("Hello Django, I'm here to fuck you up")
    return render(request, 'acountapp/hello_django.html')
