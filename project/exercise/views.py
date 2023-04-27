from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from django.shortcuts import render
from .serializers import *
from .models import *
from django.http import JsonResponse
# Create your views here.
# # Import viewsets
# from rest_framework import filters
# from rest_framework import viewsets
# # from rest_framework.filters import Se
# from rest_framework_json_api.views import RelationshipView


# Create your views here.
#user = User.objects.create_user("kalou", "123123")

@login_required(login_url='signin')
def home(request):
    return render(request, "exercise/index.html")

@login_required(login_url='signin')
def products(request):
    # Products = Product.objects.all()
    # # Context
    # context = {
    #     'Product':Products

    # }
    
    return render(request, "exercise/products.html",)

def logout(request):
    return redirect(request,'home')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        
        user = authenticate(username=username, password=passwd)

        if user is True:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('signin')
        
    return render(request, "exercise/signin.html")


def signinfffffffffff(request):
    username = request.POST.get('username')
    passwd = request.POST.get('password')
    user = authenticate(request, username=username, password=passwd)
    if user is not None:
        login(request, user)
        return redirect('home')
        # Redirect to a success page.
        ...
    else:
        return redirect('signin')
        # Return an 'invalid login' error message.
        ...

def product_table():
    result_list = list(TableData.objects.all()\
                .values('externalId', 
                        'code',
                        'description',
                        'barcode',
                        'retailPrice',
                        'wholesalePrice',
                        'discount',
                       ))
  
    return JsonResponse(result_list, safe=False)