from django.shortcuts import HttpResponse, render, redirect
import datetime

from posts.forms import PostCreateForm, ReviewCreateForm
from posts.models import Product, Categories, Review


# Create your views here.
def main(request):
    return render(request, 'layouts/index.html')


def hello(request):
    return HttpResponse("Hello! Its my project")


def now_time(request):
    return HttpResponse(f"{datetime.date.today()}")


def good_buy(request):
    return HttpResponse('Good_buy user!')


def products_view(request):
    if request.method == 'GET':
        category_id = int(request.GET.get('category_id', 0))
        if category_id:
            products = Product.objects.filter(categories__in=[category_id])
        else:
            products = Product.objects.all()

        return render(request, 'products/products.html', context={
            'products': products,
            'user': None if request.user.is_anonymous else request.user

        })


def products_detail_view(request, id):
    if request.method == 'GET':
        products = Product.objects.get(id=id)
        context = {
            'products': products,
            'reviews': products.reviews.all(),
            'categories': products.categories.all(),
            'review_form': ReviewCreateForm
        }
        return render(request, 'products/detail.html', context=context)
    if request.method == 'POST':
        products = Product.objects.get(id=id)
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            Review.objects.create(
                author=request.user,
                post_id=id,
                text=form.cleaned_data.get('text')
                # reviewtable=form.cleaned_data.get('reviewtable',True)
            )

            return redirect(f'/products/{id}/')
        else:
            return render(request, 'products/detail.html', context={
                'products': products,
                'reviews': products.reviews.all(),
                'categories': products.categories.all(),
                'review_form': form
            })


def categories_view(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'categories/index.html', context=context)


def product_create_view(request):
    if request.method == 'GET':
        return render(request, 'products/create.html', context={
            'form': PostCreateForm
        })

    if request.method == 'POST':
        form = PostCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                author=request.user,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price',0)
            )
            return redirect('/products/')
        else:
            return render(request, 'products/create.html', context={
                'form': form
            })
