from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")

def ideagained(request):
    return render(request,"idea_gained.html")

def idea(request):
    return render(request,"idea.html")

def ouridea(request):
    return render(request,"our_idea.html")

def aboutpage(request):
    return render(request,"aboutpage.html")

def register(request):
        name=request.POST['name']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        account=request.POST['account']
        message=request.POST['message']
         

        user=user.objects.create_user(name=name)
        print("we wil call back you")
        return redirect('/')
 


