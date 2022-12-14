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
from posts.views import (hello,
                         good_buy,
                         now_time, main,
                         ProductCBV,
                         ProductDetailCBV,
                         CategoriesCBV,
                         CreateFormCBV)
from users.views import LoginCBV, LogoutCBV, SignUpCBV
from django.conf.urls.static import static
from GT_products.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('hello/', hello),
    path('good_buy/', good_buy),
    path('now_time', now_time),
    path('products/', ProductCBV.as_view()),
    path('products/<int:id>/', ProductDetailCBV.as_view()),
    path('categories/', CategoriesCBV.as_view()),
    path('products/create/', CreateFormCBV.as_view()),
    path('users/login/', LoginCBV.as_view()),
    path('users/logout/', LogoutCBV.as_view()),
    path('users/register/', SignUpCBV.as_view())
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
