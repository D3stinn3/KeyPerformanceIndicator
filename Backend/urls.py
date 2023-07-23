from django.urls import path
from Backend import views

urlpatterns = [
    path('', views.index, name='home'),
    path('calendar/', views.calender, name='calendar'),
    path('kpi/', views.kpibreakdown, name='kpi')
]
