from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.






class auth_user(AbstractUser): 
    is_normal=models.BooleanField(default=True,blank=False)



class blog(models.Model):
    title=models.TextField(blank=False,max_length=100)
    subject=models.TextField(blank=False,max_length=100)
    text=models.TextField(blank=False,max_length=1500)
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

class comment(models.Model):
    comment=models.TextField(blank=False,max_length=150)
    username=models.TextField(blank=False,max_length=50,default='Unknown')
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    blogid = models.ForeignKey(blog, on_delete=models.CASCADE)

class likes(models.Model):
    text=models.TextField(blank=False,max_length=10)
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    blogid = models.ForeignKey(blog, on_delete=models.CASCADE)


    




   



    

