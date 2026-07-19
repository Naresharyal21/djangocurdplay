from django.shortcuts import render
from django.shortcuts import redirect

from .models import Myblog

from django.http import HttpResponse


# Create your views here.
def homeview(request):



  bloglogs=Myblog.objects.all().order_by("-created_at")
  

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

def blog_view(request , id):
  blog=Myblog.objects.get(pk=id)
  return  render(request,"components/Blogs.html",{
   "blog":blog 
  })

def delete_view(request ,id ):
  blog=Myblog.objects.get(pk=id)
  return  render(request,"components/Deletepage.html",{
   "blog":blog 
  })
  
def delete_view_blog(request):
  blog_id=request.POST.get("delet_blog")
  Myblog.objects.get(pk=blog_id).delete()
  return redirect("home_url")


def update_view(request ,id ):
  blog=Myblog.objects.get(pk=id)
  return  render(request,"components/update.html",{
   "blog":blog 
  })


def update_Myblog(request ,id):
 
  
  try:
    blog=Myblog.objects.get(pk=id)
    updated_title=request.POST.get("title")
    updated_caption=request.POST.get("updateblog")
    
    blog.title=updated_title
    blog.caption=updated_caption
    blog.save()
     
   
    
  except Exception as e:
   print("Myblog not created",e)
   
  else:
   print("Myblog updated sucess")
   
  return redirect("home_url")

