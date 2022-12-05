from django.contrib import admin

# Register your models here.
from api.models import Company, Employee

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name","location","types")


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name","email","company")

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Company, CompanyAdmin)

