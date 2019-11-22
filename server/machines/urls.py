from django.urls import path
from . import views

urlpatterns = [
    path('', views.MachineList.as_view()),
    path('<int:pk>/', views.MachineDetail.as_view()),
]
