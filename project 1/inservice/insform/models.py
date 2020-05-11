from django.db import models

# Create your models here.

class eqname(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class referancename(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class inservice(models.Model):
    eqname = models.ForeignKey(eqname, on_delete=models.CASCADE)
    make1 = models.CharField(max_length=30)
    srno1 = models.CharField(max_length=30)
    referancename = models.ForeignKey(referancename, on_delete=models.CASCADE)
    make2 = models.CharField(max_length=30)
    srno2 = models.CharField(max_length=30)

class test(models.Model):
    testpoint = models.CharField(max_length=15)
    deviation1 = models.CharField(max_length=15)
    deviation2 = models.CharField(max_length=15)
    difference = models.CharField(max_length=15)
    uncertainity = models.CharField(max_length=15)
    remark = models.CharField(max_length=15)
