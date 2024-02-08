
from django.contrib import admin
from django.urls import path
from optica import views

urlpatterns = [
    path('', views.mostrarIni, name='mostrar_ini'),
    path('login/', views.Inisesion, name='login'),
    path('logout',views.cerrarSesion),

    path('mostrar_form/', views.mostrarForm, name='mostrar_form'),
    path('formulario/', views.formulario, name='formulario'),
    path('listar/', views.mostrarListar, name='listar'),
    path('eliminar_producto/<int:id>/', views.eliminarProducto, name='eliminar_producto')
]

