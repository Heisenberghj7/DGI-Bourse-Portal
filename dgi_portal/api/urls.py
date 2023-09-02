from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('dashboard', DashboardView.as_view()),
    path('actionnaire', actionnaire),
    path('companies', companies),
    path('chiffres', chiffres),
    path('ratios', ratios),
    path('retourner', retourner),
    path('publications', publications),
    path('dividende', dividende),
    path('emissions', emissions),
]
