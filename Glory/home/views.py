from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'home/index.html')
    # return render(request, 'base/index.html')


def htmltrain(request):
    return render(request, 'home/html-train.html')
