from django import forms
from .models import Photo

from django import forms


class ContactForm(forms.Form):
    nom = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded',
        'placeholder': 'Nom'
    }))
    prenom = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded',
        'placeholder': 'Prénom'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded',
        'placeholder': 'E-mail'
    }))
    telephone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded',
        'placeholder': 'Téléphone'
    }))
    objet = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded',
        'placeholder': 'Objet'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded h-40',
        'placeholder': 'Rédigez votre message ici...'
    }))

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'categorie']    