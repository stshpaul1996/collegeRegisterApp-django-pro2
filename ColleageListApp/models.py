from django.db import models

# Create your models here.

class ColleageListDB(models.Model):
    colleage_name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    email = models.EmailField()
    contact_num = models.IntegerField()
    country= models.CharField(max_length=50, null=True)

