from django.db import models

class Pelerin(models.Model):
    VOCATIONS = [
        ('CARDINAL', 'Cardinal'), ('EVEQUE', 'Évêque'), ('PRETRE', 'Prêtre'),
        ('DIACRE', 'Diacre'), ('RELIGIEUX', 'Religieux/se'), ('LAIC', 'Laïc'),
    ]
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    vocation = models.CharField(max_length=20, choices=VOCATIONS)
    diocese = models.CharField(max_length=100)
    paroisse = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15) # +224...
    photo = models.ImageField(upload_to='pelerins/')
    paye = models.BooleanField(default=False)
    reference_paiement = models.CharField(max_length=100, blank=True)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
