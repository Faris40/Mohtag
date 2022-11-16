from django.db import models

# Create your models here.



class Family(models.Model):

    family_name = models.CharField(max_length=128)

    family_dis = models.TextField()


class Donation(models.Model):


    donation_type = models.CharField(max_length=128)

    donation_dis = models.TextField()

    donation_cond = models.CharField(max_length=128)

    donation_phone = models.CharField(max_length=10)
    
    

