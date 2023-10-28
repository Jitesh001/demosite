from django.shortcuts import render
from .models import Student
# Create your views here.

def show_student(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})