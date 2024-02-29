from django.shortcuts import render
#imported student model
from .models import Student
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