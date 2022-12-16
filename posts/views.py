from django.shortcuts import HttpResponse, render
import datetime
from posts.models import Product


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
        products = Product.objects.all()

        return render(requests, 'products/products.html', context={
            'products': products,

        })


def products_detail_view(requests, id):
    if requests.method == 'GET':
        products = Product.objects.get(id=id)
        context = {
            'products': products,
            'reviews': products.reviews.all()
        }
        return render(requests, 'products/detail.html', context=context)
