from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from .models import auth_user ,blog
from django.conf import settings


# Create your views here.







#explains what to do when user fill registeration form and hit submit
def registerAccount(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if (password1==password2):
            if auth_user.objects.filter(username=username).exists():
                print("Username Taken")
                messages.info(request,'user name taken')
                messages.info(request,'Enter Valid credential')
                
                return render(request,"registerAccount.html")
            elif auth_user.objects.filter(email=email).exists():
                
                print("Email Taken")
                messages.info(request,'Email taken')
                messages.info(request,'Please Enter Valid Credential')
                return render(request,"registerAccount.html")
            elif len(password1)<8:
                messages.info(request,'password must be at least 8 charactors')

            else:
                user=auth_user.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                
                user.save()



               
                return redirect('/')
                
        else:
            print("Password Doesn't Match")
            messages.info(request,'Password Does not match')
            return render(request,"registerAccount.html")
        
        return render(request,'registerAccount.html',{"first_name":first_name})

    else:
        return render(request,"registerAccount.html")


#explains what to do when user fill login form and hit submit
def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is None:
            messages.info(request,'Invalid credentials ')
            print('first if')
            return render(request,'loginpagestylish.html')
        else:
            auth.login(request,user)
            print('2nd else')
            
            return redirect('profile')   
    else:

        return render(request,'loginpagestylish.html',)

def profile(request):    
    blog_of_user=blog.objects.filter().all()
    if request.method=='POST':
        blogid=request.POST['blogid']
        blog.objects.filter(id=blogid).delete()
        blog_of_user=blog.objects.filter().all().order_by('created_at')
        return render(request,'profile.html',{'blog_of_user':blog_of_user})
    else:

    
        return render(request,'profile.html',{'blog_of_user':blog_of_user})



###################################
def writeblog(request):
    if request.method=='POST':
        title=request.POST['title']
        subject=request.POST['subject']
        text=request.POST['text']
        blogposted=blog(title=title,subject=subject,text=text,user_id=request.user.id)
        blogposted.save()
        messages.info(request,'Posted')
        return render(request,'writeblog.html')
    else:

        return render(request,'writeblog.html')



###################################
def myblogs(request):
    if request.method=='POST':
        blogid=request.POST['blogid']
        blog.objects.filter(id=blogid).delete()
        
        myblogs=blog.objects.filter(user_id=request.user.id).all()
        return render(request,'myblogs.html',{'myblogs':myblogs})
    else:
        
        myblogs=blog.objects.filter(user_id=request.user.id).all()

        return render(request,'myblogs.html',{'myblogs':myblogs})

def showblogs(request,blogid):
    
    if blog.objects.filter(id=blogid).exists():
        myblogs=blog.objects.filter(id=blogid).all()
        
        return render(request,'showblogs.html',{'myblogs':myblogs})

def editblog(request,blogid):
    if request.method=='POST':
        title1=request.POST['title']
        subject1=request.POST['subject']
        text1=request.POST['text']
        blog.objects.filter(id=blogid).update(title=title1,subject=subject1,text=text1)
        messages.info(request,'Updated !')
        blogs=blog.objects.get(id=blogid)
        return render(request,'editblog.html',{'blogs':blogs})
    else:     
        blogs=blog.objects.get(id=blogid)
        print(blogs.id)
    
   
        return render(request,'editblog.html',{'blogs':blogs})

   
#logouts
def logout(request):
    auth.logout(request)
    return redirect('/')


#what to do when user hit profile settings.

        
        

    













    







