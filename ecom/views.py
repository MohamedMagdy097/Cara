from django.shortcuts import render, redirect, reverse, get_object_or_404
from . import forms, models
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from django.contrib import messages
from django.conf import settings
from urllib.parse import urlparse
from django.http import JsonResponse

# Create your views here.
# http://localhost:8000/

def get_products(request):
    products = None
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart = product_ids.split('|')
            products = models.Product.objects.all().filter(id__in = product_id_in_cart)
    return products 

def get_length(request): 
    product_count_in_cart = 0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    return product_count_in_cart

def home(request):
    products = models.Product.objects.all()
    site = models.Site.objects.get(pk = 1)
    user = request.user
    len = get_length(request)

    context = {'site': site, 'products': products, 'user': user, 'len': len}
    response = render(request, 'index.html', context)
    
    return response
      
def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()
 
# @login_required(login_url='login')
# @user_passes_test(is_customer)
# def customer_home_view(request):
#     user = request.user
#     customer = user.customer
#     products = models.Product.objects.all()
#     site = models.Site.objects.get(pk = 1)
#     context = {'site': site, 'products': products, 'user': user, 'customer': customer}
#     return render(request, 'customer_home.html', context)
     
# def login(request):
#     error_message = ""
#     user = None
#     userForm = forms.CustomerUserForm(request.POST or None)
#     site = models.Site.objects.get(pk = 1)
#     products = models.Product.objects.all()
#     context = {'products': products, 'userForm' : userForm, 'site': site, 'user': user, 'error_message': error_message}
    
#     if request.method == 'POST':
        
#         if userForm.is_valid():
#             user = userForm.get_user()
#             if is_customer(user):
#                 login(request, user)
#                 # return render(request, 'customer-home.html', context)
#                 return HttpResponseRedirect('customer-home')
#         else:
#             error_message = "Invalid login credentials"
#     else:
#         error_message = None

    
#     response =  render(request, 'login.html', context)
#     return response
    
def register(request):
    userForm = forms.CustomerUserForm()
    customerForm = forms.CustomerForm()
    site = models.Site.objects.get(pk = 1)
    len = get_length(request)
    context = {'userForm' : userForm,'customerForm' : customerForm, 'site': site, 'len': len}
    
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST)
        customerForm = forms.CustomerForm(request.POST, request.FILES)
        
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            customer = customerForm.save(commit=False)
            customer.user = user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return render(request, 'login.html', context)
    else:
        return render(request, 'register.html', context)
    
def details(request, slug):
    product = get_object_or_404(models.Product, slug = slug)
    details = get_object_or_404(models.ProductDetail, slug = product.pk)
    site = models.Site.objects.get(pk = 1)
    len = get_length(request)
    
    products = models.Product.objects.all()
    context = {'details': details,'product': product, 'site': site, 'products': products, 'user': request.user, 'len': len}
    return render(request, 'sproduct.html', context)

def shop(request):
    products = models.Product.objects.all()
    site = models.Site.objects.get(pk = 1)
    shop = models.Shop.objects.get(pk = 1)
    user = request.user
    len = get_length(request)
    
    context = {'site': site, 'products': products, 'user': user, 'shop': shop, 'len': len}
    response = render(request, 'shop.html', context)
    
    return response

def blog(request):
    site = models.Site.objects.get(pk = 1)
    user = request.user
    len = get_length(request)
    
    context = {'site': site, 'user': user, 'len': len}
    response = render(request, 'blog.html', context)
    
    return response

def about(request):
    site = models.Site.objects.get(pk = 1)
    user = request.user
    len = get_length(request)

    context = {'site': site, 'user': user, 'len': len}
    response = render(request, 'about.html', context)
    
    return response

def contact(request):
    contact = models.Contact.objects.get(pk = 1)
    people = models.People.objects.all()
    products = models.Product.objects.all()
    site = models.Site.objects.get(pk = 1)
    len = get_length(request)
    user = request.user
    word = ""

    if request.method == 'POST':
        massageForm = forms.MassageForm(request.POST)

        if massageForm.is_valid():
            massage = massageForm.save(commit=False)
            if user.is_authenticated:
                try:
                    customer = models.Customer.objects.get(user=user)
                    massage.user = customer  # Assign the Customer instance
                    massage.save()
                    word = massage.subject + ' sent to our team successfully!'

                except models.Customer.DoesNotExist:
                    massageForm = forms.MassageForm(request.FILES)
                    word = 'You need to login first!!'
                    return render(request, 'contact.html', context)

    else:
        massageForm = forms.MassageForm()
        word = "Let'sTalk"

    context = {'massageForm': massageForm,'site': site, 'products': products, 'user': user, 'len': len, 'contact': contact, 'people': people, 'word': word}
    
    return render(request, 'contact.html', context)

def cart(request):
    products = get_products(request)
    site = models.Site.objects.get(pk = 1)
    user = request.user
    len = get_length(request)
    
    total = 0
    #for total price shown in cart
    if products:
        for p in products:
            total = total + p.price

    context = {'site': site, 'products': products, 'user': user, 'len': len, 'total': total}
    response = render(request, 'cart.html', context)
    
    return response

def addToCart(request, pk):
    products = models.Product.objects.all()
    site = models.Site.objects.get(pk = 1)
    user = request.user
    len = get_length(request)
    
    len += 1 #test
    
    context = {'site': site, 'products': products, 'user': user, 'len': len}
    response = render(request, 'index.html', context)

    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids == "":
            product_ids = str(pk)
        else:
            product_ids = product_ids + "|" + str(pk)
        response.set_cookie('product_ids', product_ids)
    else:
        response.set_cookie('product_ids', pk)
    
    
    product = models.Product.objects.get(id = pk)
    messages.info(request, product.name + ' added to cart successfully!')
    return response

def removeFromCart(request, pk):
    site = models.Site.objects.get(pk = 1)
    #for counter in cart
    length = get_length(request)
    if length != 0:
        length -= 1
    # removing product id from cookie
    total = 0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        product_id_in_cart = product_ids.split('|')
        product_id_in_cart = list(set(product_id_in_cart))
        product_id_in_cart.remove(str(pk))
        products = models.Product.objects.all().filter(id__in = product_id_in_cart)
        #for total price shown in cart after removing product
        for p in products:
            total = total + p.price

        #  for update coookie value after removing product id in cart
        value=""
        for i in range(len(product_id_in_cart)):
            if i == 0:
                value = value + product_id_in_cart[0]
            else:
                value = value + "|" + product_id_in_cart[i]
                
        context = {'products': products, 'total': total, 'len': length, 'site': site, 'user': request.user}
        response = render(request, 'cart.html', context)
        if value == "":
            response.delete_cookie('product_ids')
            
        response.set_cookie('product_ids', value)
        return response
    
def profile(request, username):
    products = models.Product.objects.all()
    site = models.Site.objects.get(pk = 1)
    user = request.user
    customer = models.Customer.objects.get(user = user)
    len = get_length(request)

    context = {'site': site, 'products': products, 'user': user, 'len': len, 'customer': customer}
    response = render(request, 'profile.html', context)

    return response