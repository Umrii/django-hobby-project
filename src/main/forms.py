from django import forms

from .models import List

class ListForm(forms.ModelForm):
    image=forms.ImageField(required=False)
    class Meta:
        model=List
        fields={'brand','model','vin','mileage','color','description','engine','transmission','image'}