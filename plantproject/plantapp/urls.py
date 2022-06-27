from . import views
from django.urls import path
app_name='plantapp'
urlpatterns = [

    path('',views.index,name="index"),
    path('login',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('plantorder',views.plantorder,name="plantorder"),
    path('plantdetails', views.plantdetails, name="plantdetails"),
    path('logout',views.logout,name="logout"),
    path('shop/',views.shop,name="shop")
]
