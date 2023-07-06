from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class Input(View):
    def post(self,request):
        x=int(request.POST["t1"])
        y=int(request.POST["t2"])
        z=x+y
        request.session['res']=z
        request.session.set_expiry(100)
        return HttpResponse("data submitted successfully")
class Display(View):
    def get(self,request):
        if request.session.has_key("res"):
            data=request.session["res"]
            return  HttpResponse("the sum is:"+str(data))
        else:
            return render(request,'home.html')
