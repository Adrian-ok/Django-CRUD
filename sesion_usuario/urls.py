from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('sign_up/', views.registrar, name='sign_up'),
]