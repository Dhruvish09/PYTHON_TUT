from django.urls import path
from app import views

urlpatterns = [
    path('get_population/', views.get_population, name='get_population'),
    path('population',views.PopulationView.as_view(),name="data",)
]


