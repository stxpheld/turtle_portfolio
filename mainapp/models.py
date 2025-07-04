from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo de la catégorie {self.categorie.nom}"