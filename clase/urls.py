from django.urls import path
from .views import UsuarioView

app_name='usuario'
urlpatterns = [
    path('', UsuarioView.as_view(), name='usuario'),
]
