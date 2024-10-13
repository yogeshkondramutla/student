from django.db import models

# Create your models here.
class student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    place=models.CharField(max_length=30)
    contact=models.BigIntegerField()

class Meta:
    db_table="student"