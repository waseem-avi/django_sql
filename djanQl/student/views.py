from django.shortcuts import render
#imported student model
from .models import Student

from .forms import StudentForm
# Create your views here.

def student_details_view(request):
    obj = Student.objects.get(id=1)
    # context = {
    #     "first_name":obj.firstname,
    #     "last_name":obj.lastname
    # }
    context = {
        "object":obj
    }
    return render(request, "student_detail.html", context)
def student_create_view(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StudentForm()
    context = {
        "form":form
    }
    return render(request, "student_create.html", context)