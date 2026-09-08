from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = [
            'nom', 'categorie', 'fournisseur', 'prix', 
            'prix_achat', 'stock', 'seuil_alerte', 'lot', 
            'date_peremption', 'image', 'description'
        ]
        widgets = {
            'date_peremption': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'placeholder': 'Pour votre sante -----------'}),
        }