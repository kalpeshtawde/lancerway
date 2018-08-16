from django.http import HttpResponse


def index(request):
    return HttpResponse("<H1>Find your first job")
