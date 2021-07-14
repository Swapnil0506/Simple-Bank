from typing import MutableSet
from django.shortcuts import render, redirect
from .models import Customer, trans_details
from datetime import datetime
from django.db.models import F
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'bank/home.html')

def about(request):
    return render(request, 'bank/about.html', {'title': 'About'})

def view_customer(request): #list of transactions
    all_entries = Customer.objects.all()
    context = {
        "cust_details" : all_entries
    }
    return render(request, 'bank/customer.html', context)

def transactions(request): #individual transaction(card)
    if request.method == "POST":
         cust = request.POST.get('submit')
         query1 = Customer.objects.get(name =cust)
         query2 = Customer.objects.exclude(name = cust)
         context = {
             "cust_name" : query1,
             "all_details" : query2,
             }
    else:
        context = {

        }
    return render(request, 'bank/transaction.html', context)

def history(request): #transaction history
    if request.method =="POST":
        receiver= request.POST.get('to')
        money = request.POST.get('amount2')
        sender = request.POST.get('submit')
        query2 = Customer.objects.get(name = sender)
        query2.amount= F('amount')- money           
        query2.save()
        query1 = Customer.objects.get(name= receiver)
        query1.amount= F('amount')+ money
        query1.save()
        result = Customer.objects.get(name = sender)
        transact = trans_details()
        transact.sender_name = sender
        transact.sender_email = result.email
        transact.sender_accno = result.account_no
        transact.current_balance = result.amount
        transact.money_transfer = money
        transact.reciever_name = receiver
        transact.date = datetime.today()
        transact.save()
        messages.success(request, f'Payment Successful! Congrats! Checkout history for transaction details.')
        return redirect('customer')
    all_entries = trans_details.objects.all()
    context = {
            "history" : all_entries
        }
    return render(request, 'bank/history.html', context)
