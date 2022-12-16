from django.shortcuts import HttpResponse, render
import datetime
from posts.models import Products


# Create your views here.
def main(request):
    return render(request, 'layouts/index.html')


def hello(request):
    return HttpResponse("Hello! Its my project")


def now_time(request):
    return HttpResponse(f"{datetime.date.today()}")


def goodby(request):
    return HttpResponse('Goodby user!')


def products_view(requests):
    if requests.method == 'GET':
        products = Products.objects.all()

        return render(requests, 'products/products.html', context={
            'products': products
        })
