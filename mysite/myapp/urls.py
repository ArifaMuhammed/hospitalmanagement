
from django.urls import path
from .import views

urlpatterns = [
    path('', views.mainhome, name='home'),
    path('login', views.login_user, name='login'),
    path('signup', views.signup, name='signup'),
    path('base/', views.index, name='base'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('doctors/', views.doct, name='doctors'),
    path('contact/', views.contact, name='contact'),
    path('department/', views.depart, name='department'),
    path('career/', views.career_view, name='career'),
    path('contact/', views.contact, name='contact'),



]