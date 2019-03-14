from django.shortcuts import render,redirect
from django.http import HttpResponse
from main.models import *


def addstudent(request):
	if(request.method=='GET'):
		return render(request,"addstudent.html",None)
	else:
		s=StudentModel()
		s.name=request.POST.get('name')
		s.gender=request.POST.get('gender')
		s.dob=request.POST.get('dob')
		s.address=request.POST.get('address')
		s.email=request.POST.get('email')
		s.phone=request.POST.get('phone')
		# save
		s.save()
		return redirect('/students/')

def displaystudents(request):
	s=StudentModel.objects.filter()
	return render(request,"DisplayStudents.html",{'students':s})

def displaystudent(request,id):
	s=StudentModel.objects.get(id=id)
	return render(request,'displaystudent.html',{'student':s})

def deletestudent(request,id):
		s=StudentModel.objects.get(id=id)
		s.delete()
		return redirect('/students/')


def updatestudent(request,id):
	if(request.method=='GET'):
		s=StudentModel.objects.get(id=id)
		return render(request,'updatestudent.html',{'student':s})
	else:
		s=StudentModel.objects.get(id=id)
		s.name=request.POST.get('name')
		s.gender=request.POST.get('gender')
		s.dob=request.POST.get('dob')
		s.address=request.POST.get('address')
		s.email=request.POST.get('email')
		s.phone=request.POST.get('phone')
		s.save()
		return redirect('/students/')


