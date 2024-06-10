from django.urls import path
from . import views

urlpatterns = [    
    path('index', views.index , name="index"),
    path('crud', views.crud, name="crud"),
    path('almunosAdd', views.alumnosAdd, name="alumnosAdd"),
    path('almunos_del/<str:pk>', views.alumnos_del, name="alumnos_del"),
    path('almunos_findEdit/<str:pk>', views.almunos_findEdit, name="alumnos_findEdit")
    
]