from django.shortcuts import render
#imported student model
from .models import Student

from .forms import StudentForm, RawStudentForm
# Create your views here.

def dynamic_lookup_view(request,id):
    obj = Student.objects.get(id=id)
    context = {
        "object":obj
    }
    return render(request, "student_detail.html", context)






def student_details_view(request):
    obj = Student.objects.get(id = 1)
    # context = {
    #     "first_name":obj.firstname,
    #     "last_name":obj.lastname
    # }
    context = {
        "object":obj
    }
    return render(request, "student_detail.html", context)
# def student_create_view(request):
#     form = StudentForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = StudentForm()
#     context = {
#         "form":form
#     }
#     return render(request, "student_create.html", context)
def student_create_view(request):
    my_form = RawStudentForm()
    if request.method == 'POST':
        my_form = RawStudentForm(request.POST)
        if my_form.is_valid():
            #now the data is good
            print(my_form.cleaned_data)
            Student.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)


    context = {
        'form' : my_form
    }
    return render(request, "student_create.html", context)