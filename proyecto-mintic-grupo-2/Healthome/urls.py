"""Healthome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from api import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('usuario/',views.UserCreateView.as_view()),
    path('usuario/<int:pk>/',views.UserDetailView.as_view()),
    path('personal-salud/',views.PersonalSaludCreateView.as_view()),
    path('personal-salud/<int:pk>/',views.PersonalSaludDetailView.as_view()),
    path('paciente/',views.PacienteCreateView.as_view()),
    path('paciente/<int:pk>/',views.PacienteDetailView.as_view()),
    path('familiar/',views.FamiliarCreateView.as_view()),
    path('familiar/<int:pk>/',views.FamiliarDetailView.as_view()),
    path('historia-clinica/',views.HistoriaClinicaCreateView.as_view()),
    path('historia-clinica/<int:pk>/',views.HistoriaClinicaDetailView.as_view()),
    path('signos-vitales/',views.SignosVitalesCreateView.as_view()),
    path('signos-vitales/<int:pk>/',views.SignosVitalesDetailView.as_view()),
    path('sugerencias/',views.SugerenciasCreateView.as_view()),
    path('sugerencias/<int:pk>/',views.SugerenciasDetailView.as_view()),
]