from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.

class Customer(models.Model): #money transfer one to one (card details)
    name= models.CharField(max_length=150)
    email= models.EmailField()
    account_no= models.CharField(max_length=20)
    ifsc_code= models.CharField(max_length=11)
    address= models.CharField(max_length=100)
    amount= models.IntegerField(max_length=10)

    def __str__(self):
        return  self.name

class trans_details(models.Model): #transaction history
    sender_name= models.CharField(max_length=150)
    sender_email= models.EmailField()
    sender_accno= models.CharField(max_length=20)
    current_balance= models.IntegerField(max_length=10)
    reciever_name= models.CharField(max_length=150)
    money_transfer= models.IntegerField(max_length=10)
    date= models.DateTimeField()


    
