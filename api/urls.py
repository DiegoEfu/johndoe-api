from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('consultar/personas/', consulta_personas),
    path('consultar/vehiculos/', consulta_vehiculos),
    path('consultar/mantenimientos/', consulta_mantenimiento),

    path('crear/persona/', crear_persona),
    path('crear/vehiculo/', crear_vehiculo),
    path('crear/mantenimiento/', crear_mantenimiento),

    path('modificar/persona/<int:pk>/', modificar_persona),
    path('modificar/vehiculo/<int:pk>/', modificar_vehiculo),
    path('modificar/mantenimiento/<int:pk>/', modificar_mantenimiento),

    path('eliminar/persona/<int:pk>/', eliminar_persona),
    path('eliminar/vehiculo/<int:pk>/', eliminar_vehiculo),
    path('eliminar/mantenimiento/<int:pk>/', eliminar_mantenimiento)
]