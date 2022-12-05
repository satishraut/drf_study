from rest_framework import viewsets
from .models import Company, Employee
from .serializer import CompanySerialzer, EmployeeSerialzer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerialzer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def employees(self,request, pk=None):
        print("Methods get employees of",pk,"company")
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emp_serialzer = EmployeeSerialzer(emps,many=True, context={'request':request})
            return Response(emp_serialzer.data)
        except Exception as err:
            print(err)
            return Response({"message":str(err)})
        

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialzer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  
