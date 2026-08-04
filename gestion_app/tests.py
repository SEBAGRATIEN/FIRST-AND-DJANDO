from django.test import TestCase

# Create your tests here.
class  User():
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

    def get_nom(self):
        return self.nom

    def get_email(self, ):
        return self.email

    def update_email(self, new_email):
        self.email = new_email


personne = User       