from django.urls import path
from . import views

urlpatterns = [
    path('feesdj/', views.django_fees),
]