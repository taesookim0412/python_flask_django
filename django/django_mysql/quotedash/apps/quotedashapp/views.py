from django.shortcuts import render, redirect
from apps.quotedashapp.models import *
from django.contrib import messages
import bcrypt

#from .models import account
# Create your views here.
def index(request):
    return render(request, "quotedashapp/index.html")

def register(request):
    errors = account.objects.acc_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    else:
        a = account()
        a.first_name = request.POST['firstname']
        a.last_name = request.POST['lastname']
        a.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        a.email = request.POST['email']
        a.save()
        request.session['id'] = a.id
        request.session['email'] = a.email
        request.session['firstname'] = a.first_name
        request.session['lastname'] = a.last_name
        return redirect('/quotes')

def login(request):
        errors = account.objects.login_validator(request.POST)
        if len(errors) > 0:
                for key, value in errors.items():
                        messages.error(request, value)
                return redirect('/')
        else:
                a = account.objects.get(email=request.POST['loginemail'])
                request.session['id'] = a.id
                request.session['firstname'] = a.first_name
                request.session['lastname'] = a.last_name
                return redirect('/quotes')
                # a = account.objects.get(email=request.POST['loginemail'])
                # if bcrypt.checkpw(request.POST['loginpassword'].encode(), a.password.encode()):
                #         return redirect('/quotes')
                # else:
                #         return redirect('/')

def quotes(request):
        context = { "quotes" : quote.objects.all() }
        return render(request, "quotedashapp/quotes.html", context)

def addquote(request):
        errors = quote.objects.quote_validator(request.POST)
        if len(errors) > 0:
                for key, value in errors.items():
                        messages.error(request, value)
                        return redirect('/quotes')
        else:
                a = request.POST['author']
                b = request.POST['quote']
                c = quote.objects.create(author=a, quote=b, email=account.objects.get(id=request.session['id']))
                c.save()
                return redirect("/quotes")

def userquotes(request, id):
        context = { "account" : account.objects.get(id=id),
                #"account" : account.objects.get(id=id)
        "quotes" : quote.objects.filter(email=account.objects.get(id=id)) }
        return render(request, "quotedashapp/userquotes.html", context)

def editaccount(request):
        id = request.session['id']
        context = { "account" : account.objects.get(id=id) }
        return render(request, "quotedashapp/editaccount.html", context)


def updateaccount(request):
        errors = account.objects.update_validator(request.POST, request.session)
        if len(errors) > 0:
                for key, value in errors.items():
                        messages.error(request, value)
                return redirect('/editaccount')
        else:
                a = account.objects.get(id=request.session['id'])
                a.email = request.POST['email']
                a.first_name = request.POST['firstname']
                a.last_name = request.POST['lastname']
                a.save()
                request.session['email'] = request.POST['email']
                request.session['firstname'] = request.POST['firstname']
                request.session['lastname'] = request.POST['lastname']
                return redirect('/editaccount')

def logout(request):
        if request.session['id']:
                del request.session['id']
                del request.session['firstname']
                del request.session['lastname']
                return redirect('/')
        return redirect('/')

def delete(request):
        quote.objects.get(id=request.POST['quoteid']).delete()
        return redirect('/quotes')