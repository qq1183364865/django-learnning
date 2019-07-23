from django.shortcuts import render,HttpResponse

# Create your views here.

def demo(request):
    return HttpResponse('<h1>hello OYYJ</h1>')