from django.urls import path
from .views import detail

app_name = 'products'

urlpatterns = [
    path('product/<slug:slug>/', detail, name='detail'),
]