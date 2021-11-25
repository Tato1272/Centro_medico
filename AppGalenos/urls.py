from django.urls import path, include
from . import views

urlpatterns = [   
    path('', views.return_base, name='base'),
]
