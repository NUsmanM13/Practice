from django.shortcuts import render

# Create your views here.


def HomePageView(request):
    ctx = {

    }
    return render(request, 'index.html', ctx)