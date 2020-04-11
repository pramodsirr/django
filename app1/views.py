from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'a.html', {'titles': 'django', 'link': ' http://127.0.0.1:8000/'})


def profile(request):
    return render(request, 'a.html', {'titles': 'profile page ', 'link': ' http://127.0.0.1:8000/'})


def expression(request):
    a = int(request.GET['text1'])
    b = int(request.GET['text2'])
    c = a + 2 * b
    return render(request, 'output.html', {'result': c})
