from django.urls import path, include
from . import views

urlpatterns = [
    path('seller_home_page/<int:id>/', views.home_page, name="home_page"),
    path('seller_order_page/<int:id>/', views.order_page, name="order_page"),
    path('seller_contact_page/<int:id>/', views.contact_seller, name="contact_seller"),
    path('seller_registration_page', views.registration_page, name="registration_page"),
    path('add_items', views.add_items, name="add_items"),
    path('login', views.seller_login, name="seller_login"),
    path('seller_logout', views.seller_logout, name="seller_logout"),
    path('go_to_shop/<int:id>/', views.go_to_shop, name="go_to_shop"),
    path('seller_home_page_render', views.seller_home_page_render, name="seller_home_page_render"),
    path('delete_order/<int:id>/', views.delete_order, name="delete_order"),
    path('accept_order/<int:id>/', views.accept_order, name="accept_order"), 
    path('delete_order_render', views.delete_order_render, name="delete_order_render"), 
    path('accept_order_render', views.accept_order_render, name="accept_order_render"), 
    path('order_page_render', views.order_page_render, name="order_page_render")
]    
 
 