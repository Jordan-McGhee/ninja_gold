from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_gold', views.process_gold),
    path('reset', views.reset)
]