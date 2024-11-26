from django.urls import path
from userapp import views

urlpatterns = [
    path('reg',views.userregisterview.as_view(),name="reg_view"),
    path('',views.userloginview.as_view(),name="log_view"),
    path('logout',views.Logoutview.as_view(),name="logout_view")
]