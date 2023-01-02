from django.urls import path

from . import views

app_name = 'system'

urlpatterns = [
    path('login/', views.login_template, name='login'),
    path('register/', views.register_template, name='register'),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_template, name='logout'),
]
