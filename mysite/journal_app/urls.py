from django.contrib import admin
from django.urls import path
from . import views
app_name = 'journal_app'
urlpatterns = [
path('',views.index,name='index'),
path('create/', views.create, name='create'),
path('<int:journal_id>/', views.edit, name='edit'),
path('<int:journal_id>/delete', views.delete, name='delete'),
path('filter/', views.filter, name='filter')
]
