from django.shortcuts import render, redirect
from apps.lit.models import *

# Create your views here.
def index(request):
    context = {"books" : book.objects.all()}
    return render(request, "lit/index.html", context)

def viewbook(request, bookid):
    context = {"book" : book.objects.get(id=str(bookid))}
    return render(request, "lit/viewbook.html", context)

def addbook(request):
    if request.method == "POST":
        a = book.objects.create(title = request.POST["title"], desc = request.POST["desc"])
        return redirect("books/" + str(a.id))

def authors(request):
        context = {"authors" : author.objects.all()}
        return render(request, "lit/authors.html", context)

def viewauthor(request, authorid):
        context = {"author" : author.objects.get(id=str(authorid))}
        return render(request, "lit/viewauthor.html", context)

def addauthor(request):
        if request.method == "POST":
                a = author.objects.create(first_name = request.POST["firstname"], last_name=request.POST["lastname"], notes = request.POST["notes"])
                return redirect("authors/" + str(a.id))