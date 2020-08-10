from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'home/home.html')
def contact(request):
    # messages.error(request,"Welcome to contact")
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        # print(name,email,phone,content)
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<5:
            messages.error(request,"Please enter valid information.")
        else:
            contact=Contact(name=name, email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Your form submitted Successfully")
    return render(request,'home/contact.html')
            

def about(request):
    return render(request,'home/about.html')
def search(request):
    query=request.GET['query']
    if len(query)>40:
        allPosts=Post.objects.none()
    else:
        allPostsTitle=Post.objects.filter(title__icontains=query)
        allPostsContent=Post.objects.filter(desc__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)
    params={'allPosts':allPosts, 'query':query}
    return render(request,'home/search.html',params)

def handleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if len(username)>15:
            messages.error(request,"Username must be under 15 characters")
            return redirect("/")
        if not username.isalnum():
            messages.error(request,"Username should only cotains letters and numbers")
            return redirect("/")
        if pass1 != pass2:
            messages.error(request,"Passwords do not match")
            return redirect("/")



        myuser = User.objects.create_user( username , email , pass1 )
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your account successfully created")
        return redirect("/")

    
    else:
        return HttpResponse("404-not found")
def handleLogin(request):
     if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user= authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"You logged in Successfully")
            return redirect("/")
        else:
            messages.warning(request,"Invalid Username and password")
            return redirect("/")
    
     return HttpResponse("404-not found")

     
def handleLogout(request):
    logout(request)
    messages.success(request,"You logged out Successfully")
    return redirect("/")
