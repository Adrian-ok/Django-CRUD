from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('añadir_personal/', views.nuevo_personal, name='nuevo_personal'),
    path('filtrar_personal/', views.filtrar_personal, name='filtrar_personal'),
    path('filtrar_personal/ver_completo/<nro_legajo>', views.ver_completo, name='verCompleto'),
    path('filtrar_personal/ver_completo/eliminar/<id>', views.eliminar, name='eliminar'),
    path('filtrar_personal/ver_completo/selectEdicion/<id>', views.selectEdicion, name='slectEdicion'),
    path('editar_personal/', views.editar_pesonal, name='editar'),
    path('vencidos/', views.vencidos, name='vencidos'),
    path('vencidos/selectEdicion/<id>', views.selectEdicion, name='slectEdicion'),
    path('filtrar_personal/reporte/', views.reportepdf, name='reporte'),
    path('vencidos/reportevenci/', views.vencipdf, name='reportevenci'),
]