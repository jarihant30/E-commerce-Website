from django.urls import path
from . import views

urlpatterns = [
    path('boss_login', views.boss_login, name="boss_login"),
    path('boss_logout', views.boss_logout, name="boss_logout"),
    path('boss_page', views.boss_page, name="boss_page"),
    path('customer_query_input', views.customer_query_input, name="customer_query_input"),
    path('customer_query', views.customer_query, name="customer_query"), 
    path('query_status/<int:id>/', views.query_status, name="query_status"),  
    path('seller_list',views.seller_list, name="seller_list"),
]   