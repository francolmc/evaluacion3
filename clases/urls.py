from django.contrib import admin
from django.urls import path
from clases import views

app_name = 'clases'

urlpatterns = [
    path('', views.home, name='home'),
    path('clases', views.ClasesListView, name='clases_list'),
    path('clases/create', views.ClasesCreateView, name='clases_create'),
    path('clases/edit', views.ClasesEditView, name='clases_edit'),
    path('clases/delete', views.ClasesDeleteView, name='clases_delete'),
    path('login', views.login, name='login')
]