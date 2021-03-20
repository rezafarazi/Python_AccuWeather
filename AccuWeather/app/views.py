from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from app.Functions import Api
import app

def Index(request):    
    context={'message':""}
    return render(request,"home.html",context)

    
def Result(request):
    context={'Value':"",'City':""}

    if(request.method=="GET"):
        city=Api.Get_Weather(request.GET.get("City"))
        context={'Value':city,'City':request.GET.get("City")}
    else:
        return HttpResponseRedirect("..")

    return render(request,"result.html",context)
