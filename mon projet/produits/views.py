from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProduitForm
from django.contrib import messages

# Vues de simple affichage pour le moment : chaque vue ne fait
# qu'afficher son template (aucune donnee de la base pour l'instant,
# ca viendra avec l'integration Django).

def home(request):
    return render(request, 'home.html')


def produits_liste(request):
    return render(request, 'produits/liste.html')


def produits_form(request,pk=None):
    produit = get_object_or_404(Produit,pk=pk) if pk else None
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            print("Produit enregistré avec succes")
            messages.success(request, "Produit enregistré avec succes")
            return redirect(produits_liste)
    else:
        form = ProduitForm(instance=produit)  

    return render(request, 'produits/formulaire.html', {'form': form, 'produit': produit})          


def stock_liste(request):
    return render(request, 'stock/liste.html')


def ventes_liste(request):
    return render(request, 'ventes/liste.html')


def ventes_form(request):
    return render(request, 'ventes/form.html')


def clients_liste(request):
    return render(request, 'clients/liste.html')


def clients_form(request):
    return render(request, 'clients/form.html')


def fournisseurs_liste(request):
    return render(request, 'fournisseurs/liste.html')


def fournisseurs_form(request):
    return render(request, 'fournisseurs/form.html')


def factures_liste(request):
    return render(request, 'factures/liste.html')


def factures_detail(request, pk):
    return render(request, 'factures/detail.html')


def statistiques(request):
    return render(request, 'statistiques/index.html')


def notifications(request):
    return render(request, 'notifications/liste.html')


def parametres(request):
    return render(request, 'parametres/index.html')


def login(request):
    return render(request, 'auth/login.html')

