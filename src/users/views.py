from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def login_view(request):
    return render(request,'views/login.html')