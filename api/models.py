from django.db import models
# Creating company models
# Create your models here.

COMPANY_TYPES = (
               ("IT","IT"),
               ("Non IT","Non IT"),
               ("Mobiles Phones","Mobile Phones")
               )
EMPLOYEE_ROLES = (("Manager","Manager"),
                  ("Software Developer","Software Developer"),
                  ("Poject lead","Project Lead"))

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=55)
    about = models.TextField()
    types = models.CharField(max_length=100, choices=COMPANY_TYPES)
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name +" "+ self.location

#Employee model
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.TextField()
    position = models.CharField(max_length=100, choices=EMPLOYEE_ROLES)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name



