from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages  # Import messages framework

from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()  # Save the form directly
            messages.success(request, 'Student added successfully!')
            return HttpResponseRedirect(reverse('index'))  # Redirect to index after success
        else:
            messages.error(request, 'Please correct the errors below.')  # Show error message
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {
        'form': form
    })

def edit(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return HttpResponseRedirect(reverse('index'))  # Redirect to index after success
        else:
            messages.error(request, 'Please correct the errors below.')  # Show error message
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
        messages.success(request, 'Student deleted successfully!')
    return HttpResponseRedirect(reverse('index'))
