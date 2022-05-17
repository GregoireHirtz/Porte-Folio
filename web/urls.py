from django.contrib import admin
from django.urls import path, include
from web.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),
    path('accueil/', accueil, name='accueil'),

    path('connexion/', connexion, name='connexion'),
    path('inscription/', inscription, name='inscription'),
    path('deconnexion/', deconnexion, name='deconnexion'),

    path('<str:slug>', projet_detail, name='projetDetail')
]
