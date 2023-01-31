from django.shortcuts import render

# Create your views here.

def homeView(request):
    tmeplate = 'index.html'
    context = {}

    return render(request, tmeplate, context)