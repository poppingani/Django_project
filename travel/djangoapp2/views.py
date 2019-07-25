from django.shortcuts import render,redirect
from django.http import HttpResponse
from djangoapp2.form import BookingForm 
# Create your views here.

def travel(request):
    return render(request,'homepage.html')

def travel2(request):
    return render(request,'packages.html')
def book(request):
    
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/confirm")
    else:
        form=BookingForm()
    return render(request,'bookingform.html',{'form':form})


def travel3(request):
    return render(request,'services.html')
def travel4(request):
    return render(request,'gallery.html')
def travel6(request):
    return render(request,'contact.html')
def travel5(request):
    return render(request,'about.html')

def confirm(request):
    return HttpResponse("<h2>Thank you! Your booking is confirmed!</h2>")
