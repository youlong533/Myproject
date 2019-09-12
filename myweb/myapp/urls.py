from django.urls import path
from . import views

urlpatterns = [
    path('bb', views.index, name="index"),
    path('case', views.case, name="case")
]
