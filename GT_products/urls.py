"""GT_products URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('products/', include('products.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import hello, good_buy, now_time, main, products_view, products_detail_view, categories_view, \
    product_create_view
from django.conf.urls.static import static
from GT_products.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('hello/', hello),
    path('good_buy/', good_buy),
    path('now_time', now_time),
    path('products/', products_view),
    path('products/<int:id>/', products_detail_view),
    path('categories/', categories_view),
    path('products/create/', product_create_view)
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
