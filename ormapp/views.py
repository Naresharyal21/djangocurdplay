from django.shortcuts import render
from django.shortcuts import redirect

from .models import Myblog

from django.http import HttpResponse


# Create your views here.
def homeview(request):



  bloglogs=Myblog.objects.all()
  

  return render(request,"components/Home.html",{
    "bloglogs":bloglogs
  })


def create_Myblog(request):
  try:
    data=request.POST
    Myblog.objects.create(
    title=data.get("title"),
    caption=data.get("caption"),
   
   )
  except Exception as e:
   print("Myblog not created",e)
   
  else:
   print("Myblog created sucess")
   
  return redirect("home_url")