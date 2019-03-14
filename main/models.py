from django.db import models

class StudentModel(models.Model):
	name=models.CharField(max_length=30)
	dob=models.CharField(max_length=30)
	gender=models.CharField(max_length=20)
	email=models.CharField(max_length=50)
	phone=models.CharField(max_length=20)
	address=models.CharField(max_length=50)


