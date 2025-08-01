from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import List
from .forms import ListForm
from users.forms import LocationForm
def main_view(request):
    return render(request,'views/main.html',{"name":"AutoMax"})


@login_required
def home_view(request):
    # print(f"Current user: {request.user}") 
    listings=List.objects.all()
    context={
        'listings': listings,
    }
    return render(request, "views/home.html", context)

@login_required
def list_view(request):
    if request.method=='POST':
        pass
    elif request.method=='GET':
        listing_form=ListForm()
        location_form=LocationForm()

    return render(request, "views/list.html", {"listing_form": listing_form, "location_form": location_form,})