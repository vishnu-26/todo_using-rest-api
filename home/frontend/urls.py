from django.urls import path,include
from . import views

urlpatterns = [
    path('feed/',views.list,name='feed'),
#    path('',views.register,name='register'),
    path('',views.login_view,name='login_view')

]
