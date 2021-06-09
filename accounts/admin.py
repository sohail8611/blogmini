from django.contrib import admin

# Register your models here.
from .models import auth_user


from .models import auth_user

admin.site.register(auth_user)
