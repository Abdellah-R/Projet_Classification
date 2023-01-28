from django import forms

class ApiForm(forms.Form):
    age = forms.IntegerField(initial=18)
    sex = forms.CharField(initial='male')
    children = forms.IntegerField(initial=4)
    smoker = forms.CharField(initial='yes')
    region = forms.CharField(initial='northeast')
    grade = forms.CharField(initial='obesity')