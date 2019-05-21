from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages

#from .models import account
# Create your views here.
Account.objects.all()
def index(request):
    Account.objects.all()
    return render(request, "loginregapp/index.html")

def register(request):
    Account.objects.all()
    errors = Account.objects.acc_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    else:
        a = Account()
        a.first_name = request.POST['firstname']
        a.last_name = request.POST['lastname']
        a.password = request.POST['password']
        a.save()
        messages.success(request, "Logged in.")
        return redirect('/success')

def success(request):
    return render(request, "loginregapp/success.html")