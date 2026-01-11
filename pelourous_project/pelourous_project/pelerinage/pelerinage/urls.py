from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('inscription/', views.inscription, name='inscription'),
    path('paiement/<int:id>/', views.paiement, name='paiement'),
    path('recu/<int:id>/', views.recu, name='recu'),
]
