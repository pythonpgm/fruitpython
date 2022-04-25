from django.urls import path
from .import views
app_name='onlineapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('fruit/<int:fruit_id>/',views.detail,name='detail'),
    path('add/',views.add_fruit,name='add_fruit'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('order/', views.order, name='order'),
path('index2/', views.index2, name='index2'),
path('logout',views.logout,name='logout'),


	]