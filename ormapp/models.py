from django.db import models

# Create your models here.
class User(models.Model):
  username=models.CharField( max_length=50 , primary_key=True)
  password=models.CharField(max_length=50)
  email=models.EmailField()
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
     return self.username

class Profile(models.Model):
    class GENDER_CHOICES(models.TextChoices):
      MALE='M','Male'
      FEMALE='F','Female'
      OTHERS='O','Others'
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    addresslines=models.CharField(max_length=50)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)


    def __str__(self):
       return self.bio


 


class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    caption=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User, through="Like")

    def __str__(self):
      return self.caption
  



class Like(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)




  




class Myblog(models.Model):
   title=models.CharField(max_length=50)
   caption=models.TextField()
   created_at=models.DateTimeField(auto_now_add=True)
   updated_at=models.DateTimeField(auto_now_add=True)


   def __str__(self):
      return self.title