from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logs', views.get_logs, name='get_logs'),
]
