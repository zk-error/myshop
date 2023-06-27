from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import registro,editarperfil

app_name = 'cuentas'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/',registro,name='registro'),
    path('editarperfil/',editarperfil,name='editarperfil'),
]
