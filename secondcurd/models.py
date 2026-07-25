from django.db import models

# Create your models here.
class User(models.Model):
  name=models.CharField(max_length=20)
  email=models.EmailField(max_length=20)
  password=models.CharField(max_length=10)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

  def __str__(self):
       return self.name
   



class Mytask(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="mytaskuser")
    blog=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
      return self.created_at
  