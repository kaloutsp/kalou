from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signin', signin, name='signin'),
    path('logout', logout, name='logout'),
    path('products', products, name='products'),
]


#path('activate/<uidb64>/<token>', views.activate, name='activate'),