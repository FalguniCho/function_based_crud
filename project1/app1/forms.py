from django import forms
from.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields ='__all__'
        labels= {
            'name':'NAME',
            'roll_no': 'ROLL NUMBER',
            'mail': 'MAIL',
            'mobileno':'MOBILE NO',
            'address':'ADDRESS',
            'dateofbirth':'DOB',
            'marks':'MARKS'

        }
        widgets={
            'mail': forms.EmailInput(attrs={'autocomplete':'off',
                                            'placeholder':'enter mail'}),
            'mobileno':forms.NumberInput(attrs={'placeholder':'eg.0000000000'}),
            'address':forms.Textarea(attrs={'placeholde':'eg.Karvenagar une 412525'}),
            'dateofbirth':forms.DateInput(attrs={'type':'date'})
        }