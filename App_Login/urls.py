from django.urls import path
from . import views

urlpatterns = [
    path('signup-page/', views.signup, name='signup'),
    path('signin-page/', views.signin, name='signin'),
    path('signout-page/', views.signout, name='signout'),
    path('', views.home, name='home'),
]
