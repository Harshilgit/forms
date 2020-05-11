from django.db import models

# Create your models here.

class lab(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class master(models.Model):
    mastername = models.CharField(max_length=100)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    rng = models.CharField(max_length=10)
    leastcount = models.CharField(max_length=10)
    uncertainity = models.CharField(max_length=10)
    idno = models.CharField(max_length=10)
    srno = models.CharField(max_length=10)
    calibrationdate = models.CharField(max_length=15)
    calibrationduedate = models.CharField(max_length=15)
    lab = models.ForeignKey(lab,on_delete=models.CASCADE)
    certificateno = models.CharField(max_length=50)


    