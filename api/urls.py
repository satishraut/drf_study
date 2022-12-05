from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CompanyViewset, EmployeeViewset

routers = DefaultRouter()

routers.register(r'companies',CompanyViewset)
routers.register(r'employee',EmployeeViewset)

urlpatterns = [
    path('',include(routers.urls))
]
