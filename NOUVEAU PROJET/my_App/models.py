from django.db import models

# Create your models here.
class Medicament(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=1)
    quantite = models.IntegerField()
    description = models.TextField(max_length=300)
    le_produit_est_actif = models.BooleanField()

    class Meta:
        verbose_name = "Medicament"
        verbose_name_plural: "Medicament"

    def __str__(self):
        return self.nom    
