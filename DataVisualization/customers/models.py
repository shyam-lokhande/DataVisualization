from django.db import models

# Create your models here.
class Customers(models.Model):
    company_name=models.CharField(max_length=220)
    budget=models.PositiveIntegerField()
    employment=models.PositiveIntegerField()
    joined=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.company_name)
