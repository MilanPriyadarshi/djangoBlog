from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    messages.success(request,"Welcome to My Blog :)")
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
    query=get.GET['get']
    print(query)
    return render(request,'home/search.html')
