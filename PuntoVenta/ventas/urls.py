from django.urls import path, include
from. import views
urlpatterns = [
    path('', views.ventas_view, name= 'Ventas'),
]

