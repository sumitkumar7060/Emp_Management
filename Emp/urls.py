from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='show'),
    path('add/', views.add, name='add'),
    path('show', views.show, name='show'),
    path('data', views.data, name='data')
]
