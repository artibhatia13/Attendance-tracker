from django.contrib import admin
from django.urls import path, include
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('webcam/', views.webcam, name='webcam'),
    path('attendance/', views.attendance, name='attendance')
]
