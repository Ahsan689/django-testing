from datetime import datetime
from django.shortcuts import render, HttpResponse
from mobileapi.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "variable1": "Harry is great",
        "variable2": "Rohan is great"
    }
    messages.success(request, "this is test messsage")
    return render(request, 'index.html', context)
    # return HttpResponse('this is HOME')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('this is About')

def services(request):
    return render(request, 'services.html')
    # return HttpResponse('this is services')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc =  request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc , date = datetime.today())
        contact.save()
        messages.success(request, "Your message sent Successfully")
    return render(request, 'contact.html')
    # return HttpResponse('this is Contact')


