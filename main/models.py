from django.db import models

class StudentModel(models.Model):
	name=models.CharField(max_length=30)
	dob=models.CharField(max_length=30,null=True,blank=True)
	gender=models.CharField(max_length=20)
	email=models.CharField(max_length=50,null=True,blank=True)
	phone=models.CharField(max_length=20,null=True,blank=True)
	address=models.CharField(max_length=50,null=True,blank=True)


