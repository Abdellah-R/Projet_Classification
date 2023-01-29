from django import forms

class ApiForm(forms.Form):
    Naics = forms.IntegerField()
    UrbanRural = forms.CharField()
    NoEmp = forms.IntegerField(initial=4)
    RetainedJob = forms.CharField()
    Term = forms.CharField()