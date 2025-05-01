from django.db import models
#-----------------------------------------------------------------------
class Profile(models.Model):
    ism =models.CharField(max_length=255)
    yosh = models.PositiveSmallIntegerField()
    sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ism
#----------------------------------------------------------------------
class Kurs(models.Model):
    nom =models.CharField(max_length=255)
    daraja = models.CharField(max_length=50)
    ustoz = models.CharField(max_length=255)
    narx = models.FloatField()
    chegirma = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.nom
#----------------------------------------------------------------------
class Izoh(models.Model):
    profil = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    kurs = models.ForeignKey(Kurs, on_delete=models.SET_NULL, null=True)
    matn = models.TextField()
    sana = models.DateField(auto_now_add=True)
    baho = models.CharField()

    def __str__(self):
        return f"{self.profil}"
#----------------------------------------------------------------------
class Tanlangan(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.SET_NULL, null=True)
    profil = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.kurs}"
#----------------------------------------------------------------------
class Xarid(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.SET_NULL, null=True)
    profil = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    sana = models.DateField(auto_now_add=True)
    holat = models.CharField(max_length=255)

    def __str__(self):
        return f" {self.kurs}"
#----------------------------------------------------------------------