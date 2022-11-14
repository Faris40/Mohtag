from django.db import models

# Create your models here.



class Family(models.Model):

    family_name = models.CharField(max_length=128)

    family_dis = models.TextField()

    
    

