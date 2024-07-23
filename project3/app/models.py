from django.db import models

# Create your models here.
class Emp(models.Model):
    EID=models.CharField(max_length=50)
    Ename=models.CharField(max_length=50)
    sal=models.CharField(max_length=50)
    deptno=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Ename
