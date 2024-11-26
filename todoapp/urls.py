from django.urls import path
from todoapp import views

urlpatterns = [
    # path('add',views.addtodo.as_view(),name="add_todo"),
    path('home',views.home.as_view(),name="home_view"),
    path('list',views.listtodo.as_view(),name="list_view"),
    path('delect/<int:id>',views.delecttodo.as_view(),name="del_view"),
    path('edit/<int:id>',views.edittodo.as_view(),name="edit_view"),
]