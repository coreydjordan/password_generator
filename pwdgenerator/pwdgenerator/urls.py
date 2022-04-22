from django.contrib import admin
from django.urls import path
from generator import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home/password/', views.password, name='password'),
]
