from django.urls import path
from . import views

urlpatterns = [
    # path('' , views.profile, name='profile'),
    path('login' , views.loginUser, name='login'),
    path('register' , views.register, name='register'),
    path('logout' , views.logoutUser,name='logout' ),
    path('dashboard', views.dashboard, name='dashboard'),
    path('url-delete/<id>', views.deleteURL, name='delete')
]
