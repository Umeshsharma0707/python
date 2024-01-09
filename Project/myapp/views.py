from django.shortcuts import render
from django.http import HttpResponse
from .models import *
"""
Django ORM :

get(): fetch data from model and return an object but only single records
       if there are multiple records founds with given condition it will
       thrown an exception

"""

# Create your views here.
def home(request):
    return render(request,"myapp/index.html")

def login(request):
    if request.POST:
        
        try:

            p_email = request.POST["email"]
            p_password = request.POST["password"]
            print("email : ",p_email)
            print("password : ",p_password)

            uid = User.objects.get(email = p_email,password = p_password)
            print("object : ", uid)
            print("email : " , uid.email)
            print("role : " , uid.role)
            # chairman id 
            cid = Chairman.objects.get(userid = uid)
            print("first name : ",cid.firstname)
            return render(request,"myapp/index.html")
        except Exception as e:
            print("Exception :>>>>>>>>>>>>> : ",e)
            e_msg = "invalid pass"
            return render(request,"myapp/index.html",{ "emsg": e_msg})

    else:
        print("page loaded")

        return render(request,"myapp/index.html")
    