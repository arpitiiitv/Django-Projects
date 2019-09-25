from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request , 'shop/index.html')


def about(request):
    pass

def contact(request):
    pass
def tracker(request):
    pass

def search(request):
    pass

def checkout(request):
    pass

def productview(request):
    pass


