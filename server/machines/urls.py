from django.urls import path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register('', views.MachineViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('', views.MachineList.as_view()),
    path('<int:pk>/', views.MachineDetail.as_view()),
]