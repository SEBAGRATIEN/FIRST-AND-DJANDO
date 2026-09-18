from django import forms
from .models import Produit, Client, Fournisseur

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = [
            'nom', 'categorie', 'fournisseur', 'prix', 
            'prix_achat', 'stock', 'seuil_alerte', 'lot', 
            'date_peremption', 'actif', 'image', 'description'
        ]
        widgets = {
            'date_peremption': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'placeholder': 'Pour votre sante -----------'}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'email', 'telephone', 'adresse', 'date_naissance', 'note']  

        widgets = {
            'adresse': forms.Textarea(attrs={'placeholder': 'Adresse du client',}),
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={
                'placeholder': 'Informmation utile pour le pharmacien',
                }),
        }  

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'telephone', 'contact', 'email', 'adresse', 'notes', 'actif', ]
        widgets = {
            'adresse': forms.Textarea(attrs={
                'placeholder': 'Adresse du fournisseur',
                }),
            'notes': forms.Textarea(attrs={
                'placeholder': 'Composition, posologie, precautions'
            }),   
        }       