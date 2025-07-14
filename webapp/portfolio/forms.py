from django import forms

class PortfolioForm(forms.Form):
    file = forms.FileField()