from django.shortcuts import render,redirect
from userapp.forms import userregisterform,userloginform
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views.generic  import TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.

# class userregisterview(View):
#     def get(self,request,*args,**kwargs):
#         form=userregisterform()
#         return render(request,'user_register.html',{'forms':form})
    

    # def post(self,request,*args,**kwargs):
    #     form=userregisterform(request.POST)
    #     if form.is_valid():
    #         form_data=form.cleaned_data
    #         User.objects.create_user(**form_data)
    #         messages.success(request,"registration successful")
    #         return redirect ('log_view')
    #     else:
    #         messages.warning(request,"invalid input")
    #         return redirect("reg_view")

class userregisterview(CreateView):  
    template_name='user_register.html'
    form_class=userregisterform
    model=User
    # success_url=reverse_lazy('log_view')

    def form_valid(self,form):
         messages.success(self.request,"registration successful")
         User.objects.create_user(**form.cleaned_data)
        #  return super().form_valid(form)
         return redirect('log_view')
    



     







        
class userloginview(View):
    
    def get(self,request,*args,**kwargs):
        form=userloginform()
        return render(request,'user_login.html',{'forms':form})
    def post(self,request,*args,**kwargs):
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
            messages.success(request,"registration successful")
            return render(request,'home.html')

        else:
            messages.warning(request,"invalid input")
            return redirect('log_view')
        
class Logoutview(View):
        def get(self,request):
            logout(request)
            messages.success(request,"logout successful")
            return redirect('log_view')

        

        

            





