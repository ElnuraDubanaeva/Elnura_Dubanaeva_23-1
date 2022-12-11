from django.shortcuts import HttpResponse
import datetime


# Create your views here.
def main(request):
    return HttpResponse(f'{request.path},{request.method}')


def hello(request):
    return HttpResponse("Hello! Its my project")


def now_time(request):
    return HttpResponse(f"{datetime.date.today()}")


def admin(request):
    return HttpResponse(f'{request.method}',
                        {request.path})


def goodby(request):
    return HttpResponse('Goodby user!')
