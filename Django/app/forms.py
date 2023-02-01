from django import forms
from django.core.validators import MinValueValidator

class ApiForm(forms.Form):
    NAICS = forms.ChoiceField(choices=[
        (0,  'Autre'),
        (11, "Agriculture, sylviculture, pêche et chasse"), 
        (21, "Exploitation minière"), 
        (22, "Services publics"), 
        (23, "Construction"),
        (31, "Fabrication"),
        (42, "Commerce de gros"), 
        (44, "Commerce de détail"), 
        (48, "Transport et entreposage"), 
        (51, "Informations"), 
        (52, "Finance et assurance"), 
        (53, "Location et bail de biens immobiliers"), 
        (54, "Services professionnels, scientifiques et techniques"), 
        (55, "Gestion de sociétés et entreprises"), 
        (56, "Administration générale et de soutien et gestion des déchets et remédiation"), 
        (61, "Services éducatifs"), 
        (62, "Soins de santé et assistance sociale"), 
        (71, "Arts, divertissement et loisirs"), 
        (72, 'Hébergement et restauration'),
        (81, 'Services de nettoyage et de sécurité'), 
        (92, 'Administration publique')
    ], 
        widget=forms.Select(attrs={'class': 'naics-field'}) )
    

    UrbanCHOICES = [(0, 'Urbain'), (1, 'Rural'), (2, 'Autre')]
    UrbanRural = forms.ChoiceField(choices=UrbanCHOICES, widget=forms.RadioSelect, initial='Existing')
   
    NoEmp = forms.IntegerField(validators=[MinValueValidator(0)])
    RetainedJob = forms.IntegerField(validators=[MinValueValidator(0)])
    Term = forms.IntegerField(validators=[MinValueValidator(0)])