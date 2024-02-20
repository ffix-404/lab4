from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def Defult_path(request):
    return render(request,"hello.html")

def anyNumber(request,price):

    return HttpResponse(f"the total tax is = {(int(price)*(15/100))+int(price)}!")

def taxrate(request,taxrate1):

    return render(request,"tax.html",{"taxrate1":taxrate1})