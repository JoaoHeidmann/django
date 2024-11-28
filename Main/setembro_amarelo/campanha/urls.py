from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('campanha/', views.campanha, name='campanha'),
    path('depoimentos/', views.depoimentos, name='depoimentos'),
    path('contatos/', views.contatos, name='contatos'),
]