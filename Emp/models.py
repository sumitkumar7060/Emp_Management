from django.db import models

# Create your models here.


class Employee(models.Model):
    Name = models.CharField(max_length=200, null=True)
    Role = models.CharField(max_length=200, null=True)
    Mobile = models.BigIntegerField(null=True)
    Manager = models.CharField(max_length=200, null=True)
    Office = models.CharField(max_length=200, null=True)
    Joining_date = models.DateField()

    def __str__(self):
        return self.Name
