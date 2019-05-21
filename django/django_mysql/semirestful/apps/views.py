from django.shortcuts import redirect, render
from apps.shows.models import *

def new(request):
    if (request.method == "GET"):
        return render(request, "new.html")

def create(request):
    if (request.method == "POST"):
        return redirect("shows/" .id)

def show(request, showid):
    if (request.method == "GET"):
        return render(request, "showid.html")

def index(request):
    if (request.method == "GET"):
        return render(request, "shows.html")

def edit(request, showid):
    if (request.method == "GET"):
        return render(request, "editshow.html")

def update(request, showid):
    if (request.method == "POST"):
        return redirect("shows/" + str(showid))

def destroy(request, showid):
    if (request.method == "GET"):
        return redirect("shows/" + str(showid))