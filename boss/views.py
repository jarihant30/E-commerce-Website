from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from .models import BossTable, CustomerQuery


def boss_logout(request):
    logout(request)
    return render(request,'boss/boss_login.html') 


def boss_login (request):
    return render(request,'boss/boss_login.html')

def boss_page (request):
    if request.method == "POST":
        boss_name = request.POST['login_username']
        boss_password  = request.POST['login_password']

        user = authenticate(username = boss_name , password = boss_password)

        if user is not None:

            boss_user = BossTable.objects.filter(boss_name = boss_name)

            if len(boss_user) != 0 :
                login(request, user)
                return render(request, 'boss/boss_page.html')
            else:
                return HttpResponse("not a boss !!")
        else:
            return HttpResponse("not a valid user !!")
    else:
        return HttpResponse(" who are you ??? ")

def seller_list (request):
    return render(request, 'boss/seller_list.html')


def query_status(request, id):

    CustomerQuery.objects.filter(id = id).update(query_status = "2")

    customer_email = CustomerQuery.objects.all()

    params = {
        'customer_query' : customer_email
    }

    return render(request, 'boss/customer_query.html', params)

def customer_query(request):

    customer_email = CustomerQuery.objects.all()

    params = {
        'customer_query' : customer_email ,
    }

    return render(request, 'boss/customer_query.html', params)

def customer_query_input (request):

    customer_email = request.GET['email_address']
    customer_query = request.GET['customer_query']

    ins = CustomerQuery(customer_email = customer_email, customer_query = customer_query).save()

    return redirect('/')