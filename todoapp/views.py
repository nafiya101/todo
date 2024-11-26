from django.shortcuts import render,redirect
from todoapp.forms import todoform,todoeditform
from todoapp.models import Todos
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView

# Create your views here.
# class home(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,'home.html')
class home(TemplateView):
    template_name='home.html'




# class addtodo(View):
#     def get(self,request,*args,**kwargs):
#         form=todoform()
#         return render(request,"add_todo.html",{"forms":form})
#     def post(self,request,*args,**kwargs):
#         form=todoform(request.POST)
#         if form.is_valid():
#             user=request.user
#             title=form.cleaned_data.get("title")
#             desc=form.cleaned_data.get("description")
#             Todos.objects.create(title=title,description=desc,user=user)
#             messages.success(request,"task add succesfully")
#             return redirect("home_view")
#         else:
#             return HttpResponse("invalid data")
        

class listtodo(View):
    
    def get(self,request,*args,**kwargs):
        todos=Todos.objects.filter(user=request.user)
        return render(request,"list_todo.html",{'todos':todos})
    
class delecttodo(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=Todos.objects.get(id=id)
        todo.delete()
        return redirect("list_view")
    
class edittodo(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=Todos.objects.get(id=id)
        form=todoeditform(instance=todo)
        return render(request,"edit_todo.html",{'form':form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=Todos.objects.get(id=id)
        form=todoeditform(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list_view')



        

    




