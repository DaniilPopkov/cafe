from django import forms
from cafe_site.models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        widgets ={
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'text':forms.Textarea(attrs={'class': 'form-control'}),
            'portion':forms.TextInput(attrs={'class': 'form-control'}),
            'price':forms.TextInput(attrs={'class': 'form-control'}),
        }