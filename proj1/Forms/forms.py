# I have created this file and is currently of no use.

# from django import forms  
# class StudentForm(forms.Form):  
#     # firstname = forms.CharField(label="Enter first name",max_length=50)  
#     # lastname  = forms.CharField(label="Enter last name", max_length = 10)  
#     # email     = forms.EmailField(label="Enter Email")  
#     file      = forms.FileField() # for creating file input  
from django import forms
  
# creating a form 
class GeeksForm(forms.Form):
    geeks_field = forms.DecimalField(max_length = 200)