from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'id',
            'firstname',
            'lastname',
            'passed'
        ]

class RawStudentForm(forms.Form):
    id        = forms.IntegerField()
    firstname = forms.CharField()
    lastname  = forms.CharField()
