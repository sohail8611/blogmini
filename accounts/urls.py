from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .models import auth_user
from django.conf.urls import url



  




urlpatterns = [
    path('', views.home,name='home'),
    path('accounts/register',views.registerAccount,name='registerAccount'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('writeblog',views.writeblog,name='writeblog'),
    path('myblogs',views.myblogs,name='myblogs'),
    path('showblogs/<int:blogid>',views.showblogs,name='showblogs'),
    path('myblogs/edit/<int:blogid>',views.editblog,name='edit'),
    path('showblogs/like/<int:blogidd>',views.like,name='showblogs')
    

    
  
   
]
