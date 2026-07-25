from django.shortcuts import render ,redirect 
from django.http import HttpResponse

from .models import User

# Create your views here.
def signup(request):
  if request.method=="POST":
    uname=request.POST.get("username")
    uemail=request.POST.get("useremail")
    upassword=request.POST.get("userpassword")


    if(User.objects.filter(email=uemail).exists()):
     return redirect("signin_view_url")

    

    User.objects.create(
     name=uname,
     email=uemail,
     password=upassword
     )
    
    
    return redirect("signin_view_url")
  
  return render(request,"components/Signup.html") 



def signin(request):
  if request.method== "POST":


   l_email=request.POST.get("useremail")
   l_password=request.POST.get("userpassword")
   if User.objects.filter(email=l_email,password=l_password).exists():
    return redirect("home_url")
 
  return render(request,"components/Login.html")



def home(request):
  # user_data=User.objects.filter(email=request.POST.get("useremail"))
  user_data=User.objects.all()
  print(user_data)
  
  return render(request,"components/Home.html",{
    "user_data":user_data
   
  })

def delete_user(request):

  if request.method=="POST":
   user_id=request.POST.get("user_id")
   User.objects.filter(pk=user_id).delete()
   return redirect("signup_view_url")
  

  return redirect("home_url")
  

def update_user(request):
   if request.method== "POST":
    id=request.POST.get("user_id")
   
    updating_data=User.objects.get(pk=id)
  
   
    if request.POST.get("useremail"):
      uname=request.POST.get("username")
      uemail=request.POST.get("useremail")
      upassword=request.POST.get("userpassword")
      if User.objects.filter(email=uemail).exists():
       return redirect("home_url")

      updating_data.name=uname
      updating_data.email=uemail
      updating_data.password=upassword
      updating_data.save()

      return redirect("home_url")
  
   return render(request,"components/update.html",{
     "data":updating_data
     
   })
  



 
 