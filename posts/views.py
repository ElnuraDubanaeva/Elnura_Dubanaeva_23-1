from django.db.models import Manager
from django.shortcuts import HttpResponse, render, redirect
import datetime

from posts.forms import PostCreateForm, ReviewCreateForm
from posts.models import Product, Categories, Review
from posts.constants import PAGINATION_LIMIT
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.


def hello(request):
    return HttpResponse("Hello! Its my project")


def now_time(request):
    return HttpResponse(f"{datetime.date.today()}")


def good_buy(request):
    return HttpResponse('Good_buy user!')


def main(request):
    return render(request, 'layouts/index.html')


class ProductCBV(ListView):
    queryset = Product.objects.all()
    template_name = 'products/products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'products': kwargs['products'],
            'max_page': kwargs['max_page'],
            'user': kwargs['user']
        }

    def get(self, request, **kwargs):
        category_id = int(request.GET.get('category_id', 0))
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if category_id:
            products = Product.objects.filter(categories__in=[category_id])
        else:
            products = self.queryset.all()
        if search:
            products = products.filter(title__icontains=search)
        # products = products.order_by('-created_date')

        max_page = products.__len__() // PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1

        max_page = int(max_page)

        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]
        return render(request, self.template_name, self.get_context_data(
            products=products,
            user=None if request.user.is_anonymous else request.user,
            max_page=range(1, max_page + 2)))


# def products_view(request):
#     if request.method == 'GET':
#         category_id = int(request.GET.get('category_id', 0))
#         search = request.GET.get('search')
#         page = int(request.GET.get('page', 1))
#
#         if category_id:
#             products = Product.objects.filter(categories__in=[category_id])
#         else:
#             products = Product.objects.all()
#
#         products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]
#
#         if search:
#             products = products.filter(title__icontains=search)
#         # products = products.order_by('-created_date')
#
#         max_page = round(products.__len__() / PAGINATION_LIMIT)
#         if round(max_page) < max_page:
#             max_page = round(max_page) + 1
#
#         return render(request, 'products/products.html', context={
#             'products': products,
#             'user': None if request.user.is_anonymous else request.user,
#             'max_page': range(1, max_page + 1)
#         })


class ProductDetailCBV(DetailView, CreateView):
    queryset = Product.objects
    template_name = 'products/detail.html'
    form_class = ReviewCreateForm

    def get_context_data(self, **kwargs):
        return {
            'products': kwargs['products'],
            'categories': kwargs['categories'],
            'reviews': kwargs['reviews'],
            'review_form': kwargs['review_form'],
            'user': kwargs['user']
        }

    def get(self, request, id=None, **kwargs):
        products = self.queryset.get(id=id)
        return render(request, self.template_name, self.get_context_data(
            products=products,
            reviews= products.reviews.all(),
            categories= products.categories.all(),
            review_form= ReviewCreateForm,
            user= request.user if not request.user.is_anonymous else None
        ))

    def post(self, request, id=None, **kwargs):
        products = self.queryset.get(id=id)
        form = self.form_class(data=request.POST)
        if form.is_valid():
            Review.objects.create(
                author=request.user,
                post_id=id,
                text=form.cleaned_data.get('text')
            )

            return redirect(f'/products/{id}/')
        else:
            return render(request, self.template_name, self.get_context_data(
                products=products,
                reviews=products.reviews.all(),
                categories=products.categories.all(),
                review_form=form
            ))


#
# def products_detail_view(request, id):
#     if request.method == 'GET':
#         products = Product.objects.get(id=id)
#         context = {
#             'products': products,
#             'reviews': products.reviews.all(),
#             'categories': products.categories.all(),
#             'review_form': ReviewCreateForm,
#             'user': request.user if not request.user.is_anonymous else None
#         }
#         return render(request, 'products/detail.html', context=context)
#     if request.method == 'POST':
#         products = Product.objects.get(id=id)
#         form = ReviewCreateForm(data=request.POST)
#         if form.is_valid():
#             Review.objects.create(
#                 author=request.user,
#                 post_id=id,
#                 text=form.cleaned_data.get('text')
#             )
#
#             return redirect(f'/products/{id}/')
#         else:
#             return render(request, 'products/detail.html', context={
#                 'products': products,
#                 'reviews': products.reviews.all(),
#                 'categories': products.categories.all(),
#                 'review_form': form
#             })


class CategoriesCBV(DetailView):
    queryset = Categories.objects.all()
    template_name = 'categories/index.html'

    def get(self, request):
        return render(request, self.template_name, context={
            'categories': self.queryset,
            'user': request.user if not request.user.is_anonymous else None
        })


# def categories_view(request):
#     if request.method == 'GET':
#         categories = Categories.objects.all()
#         context = {
#             'categories': categories,
#             'user': request.user if not request.user.is_anonymous else None
#         }
#         return render(request, 'categories/index.html', context=context)


class CreateFormCBV(CreateView, FormView):
    template_name = 'products/create.html'
    form_class = PostCreateForm
    success_url = '/products/'

    def get_context_data(self, **kwargs):
        return {
            'form': kwargs['form']
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(
            form=PostCreateForm,
        ))

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(data=request.POST)
        if form.is_valid():
            Product.objects.create(
                author=request.user,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price', 0)
            )
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, context={
                'form': form
            })

# def product_create_view(request):
#     if request.method == 'GET':
#         return render(request, 'products/create.html', context={
#             'form': PostCreateForm,
#         })
#
#     if request.method == 'POST':
#         form = PostCreateForm(data=request.POST)
#
#         if form.is_valid():
#             Product.objects.create(
#                 author=request.user,
#                 title=form.cleaned_data.get('title'),
#                 description=form.cleaned_data.get('description'),
#                 price=form.cleaned_data.get('price', 0)
#             )
#             return redirect('/products/')
#         else:
#             return render(request, 'products/create.html', context={
#                 'form': form
#             })
