from django import forms

class getInfo(forms.Form):
    director = forms.CharField(max_length=50)
    genre1 = forms.CharField(max_length=50)
    genre2 = forms.CharField(max_length=50)
    actor1 = forms.CharField(max_length=50)
    actor2 = forms.CharField(max_length=50)
    actor3 = forms.CharField(max_length=50)
    actor4 = forms.CharField(max_length=50)
    actor5 = forms.CharField(max_length=50)
    actor6 = forms.CharField(max_length=50)
