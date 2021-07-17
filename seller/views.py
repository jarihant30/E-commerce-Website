
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from costomer.models import state , city
from .models import seller_shop_details, products , order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from  .models import seller_shop_details

def accept_order(request , id):

    order.objects.filter(id = id).update(order_status = "1")

    return redirect('accept_order_render')
 

def accept_order_render(request):

    Seller = seller()
    seller_id = seller_shop_details.objects.get( id = Seller)
    seller_name = seller_shop_details.objects.get( full_name = seller_id.full_name)
    seller_orders = order.objects.filter(seller_name = seller_name)

    params = {
        'id':Seller,
        'seller_orders' : seller_orders
    }

    return render(request, 'seller/seller_order_page.html', params)


 
def delete_order(request,id):

    order.objects.filter(id = id).update(order_status = "2")

    return redirect('delete_order_render')

def delete_order_render(request):

    Seller = seller()
    seller_id = seller_shop_details.objects.get( id = Seller)
    seller_name = seller_shop_details.objects.get( full_name = seller_id.full_name)
    seller_orders = order.objects.filter(seller_name = seller_name)

    params = {
        'id':Seller,
        'seller_orders' : seller_orders
    }

    return render(request, 'seller/seller_order_page.html', params)
 
def go_to_shop(request, id): 

    seller_product_id = products.objects.filter(shop_name_id = id)
    seller_id  = seller_shop_details.objects.get(id = id)
    seller_name  = seller_shop_details.objects.get(full_name = seller_id.full_name)

    params = {
        'seller_name' : seller_name,
        'seller_product_id' : seller_product_id,
        'id' : seller_name.id,
        'user' : 'costomer'
    } 
        
    return render(request, 'seller/seller_home_page.html', params)
 

def seller_logout(request):
    logout(request)
    return redirect('/')

def seller_login(request):

    if request.method == "POST":

        username  = request.POST['login_username']
        password = request.POST['login_password']

        user = authenticate(username = username , password = password)

        if user is not None:

            confirm_seller = seller_shop_details.objects.filter(full_name = username)

            if len(confirm_seller) !=0:

                login(request , user)
  
                seller_name = seller_shop_details.objects.get(full_name__iexact = username)
                seller_product_id = products.objects.filter(shop_name_id = seller_name.id)
                global var
                def var():
                    return username
                params = {
                    'seller_name' : seller_name,
                    'seller_product_id' :seller_product_id,
                    'user' : 'seller',
                    'id' : seller_name.id
                }
                return redirect('seller_home_page_render')
                # return render(request, 'seller/seller_home_page.html',params)

            else:
                return HttpResponse("you are not a seller my boy")
        else:
            return HttpResponse("not a seller")
    

def home_page(request , id): 
    if request.method =="POST":
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_description = request.POST['product_description']
        shop_name = request.POST['shop_name']
        product_image = request.FILES.get('product_image')

        seller_name  = seller_shop_details.objects.get(full_name = shop_name)

        ins = products(product_name = product_name , product_price = product_price, 
                        product_description = product_description,
                        shop_name_id = seller_name.id , product_image = product_image)
        ins.save()

        seller_product_id = products.objects.filter(shop_name_id = seller_name.id)

        global var
        def var():
            return shop_name

        params = {
            'seller_name' : seller_name,
            'seller_product_id' : seller_product_id,
            'id' : seller_name.id
        }

        # return render(request, 'seller/seller_home_page.html',params)
        return redirect('seller_home_page_render')
    else:
        seller_id = seller_shop_details.objects.get(id = id)
        seller_name = seller_shop_details.objects.get(full_name = seller_id.full_name)
        seller_product_id = products.objects.filter(shop_name_id = seller_name.id)

        def var():
            return seller_name 

        params = {
            'seller_name' : seller_name,
            'seller_product_id' : seller_product_id,
            'id' : id
        }
        return redirect('seller_home_page_render')
        # return render(request, 'seller/seller_home_page.html', params)
        # return redirect('seller_home_page_render')

def seller_home_page_render(request):
    seller = var()
    seller_name = seller_shop_details.objects.get(full_name = seller)
    seller_product_id = products.objects.filter(shop_name_id = seller_name.id)

    params = {
            'seller_name' : seller_name,
            'seller_product_id' : seller_product_id,
            'id' : seller_name.id
        }
    return render(request, 'seller/seller_home_page.html',params)


def registration_page(request):

    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        states = request.POST['input_state']
        citys = request.POST['input_city']
        zip_code = request.POST['input_zip']
        shop_address = request.POST['shop_address']
        shop_cat = request.POST['shop_cat']
        seller_image = request.FILES.get('seller_image') 
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        shop_description = request.POST['shop_description']


        state_id = state.objects.get(state_name = states)
        city_id = city.objects.get(city_name = citys)

        myuser = User.objects.create_user(full_name, email, password)
        myuser.save() 

        ins = seller_shop_details(full_name = full_name , email = email , phone_number = phone_number , state = state_id, city = city_id,
                                 zip_code = zip_code, shop_address = shop_address , shop_category = shop_cat ,
                                 password = password , confirm_password = confirm_password , shop_description = shop_description,
                                  seller_image = seller_image)
        ins.save()

        params = {
            'success' : 'shop registered successfully'
        }

        return render(request, 'costomer/home_page.html', params)

    states = state.objects.all()
    cities = city.objects.all()
    params = {
        'all_state' : states,
        'all_city' : cities
    }
    return render(request, 'split.html', params)

def order_page(request , id):
    if request.method == "POST":
        seller_id = seller_shop_details.objects.get( id = id)
        seller_name = seller_shop_details.objects.get( full_name = seller_id.full_name)
        seller_orders = order.objects.filter(seller_name = seller_name)

        global seller
        def seller():
            return id

        global seller_shop_id 
        def seller_shop_id():
            return id


        params={
            'id':id,
            'seller_orders' : seller_orders
        }

        # redirect('order_page_render')

        return render(request, 'seller/seller_order_page.html',params)
    else:
        return HttpResponse("error 404")

def order_page_render(request):

    id = seller_shop_id()
    seller_id = seller_shop_details.objects.get( id = id)
    seller_name = seller_shop_details.objects.get( full_name = seller_id.full_name)
    seller_orders = order.objects.filter(seller_name = seller_name)

    params={
        'id':id,
        'seller_orders' : seller_orders
    }

    return render(request, 'seller/seller_order_page.html',params)

def contact_seller(request , id):
    params={
        'id':id
    }
    return render(request, 'seller/seller_contact_page.html', params)

def add_items(request):

    return render(request,'seller/add_items.html')
  