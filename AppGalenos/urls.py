from django.urls import path, include
from . import views

urlpatterns = [   
    path('', views.return_home, name='home'),
    
    path('listar_hora/<int:id_medico>', views.listar_hora, name="listar_hora"),

    path('add_hora', views.add_hora, name="add_hora"),

    path('editar_hora/<int:id_hora>', views.editar_hora, name="editar_hora"),

    path('borrar_hora/<int:id_hora>', views.borrar_hora, name="borrar_hora"),

    path('lista_medico', views.lista_medico, name="lista_medico"),
]
