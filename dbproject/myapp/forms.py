from django import forms

from .models import Employee


class myForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


