from django.urls import path, include
from . import views

urlpatterns = [   
    path('', views.return_home, name='home'),
    
    path('listar_hora', views.listar_hora, name="listar_hora"),

    path('add_hora', views.add_hora, name="add_hora"),
]
