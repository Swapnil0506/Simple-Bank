from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='bank-home'),
        path('about/', views.about, name='bank-about'),
        path('view-customer/', views.view_customer, name='customer'),
        path('transaction/', views.transactions, name='transaction'),
        path('history/', views.history, name='history'),
    ]