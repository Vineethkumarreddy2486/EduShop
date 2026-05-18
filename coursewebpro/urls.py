"""
URL configuration for coursewebpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('',getdata,name='getdata'),
    path('course/',course_view,name='course'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('register/',register,name='register'),
    path('profile/',profile,name='profile'),
    path('addtocart/<int:id>',AddToCart,name='addtocart'),
    path('cart/',Cart_view,name='cart'),
    path('cartremove/<int:id>',Cart_remove,name='cartremove'),
    path('delcart/<int:id>',Cart_delete,name='delcart'),
    path('search/',search_bar,name='search')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_DIR)   not needed because we are using whitenoise to serve static files in production.