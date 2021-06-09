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

    




   



    

