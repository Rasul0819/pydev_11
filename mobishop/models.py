from django.db import models

# Create your models here.


class Mobi(models.Model):
    name = models.CharField(max_length=55,
                            verbose_name='Марка телефона:')
    camera = models.CharField(max_length=55,
                              verbose_name='Камера телефона:')
    memory = models.CharField(max_length=55)
    year_realised = models.DateTimeField()
    price = models.DecimalField(decimal_places=3,max_digits=7)
    image = models.ImageField(upload_to='static/images',
                              null=True,blank=True)


    
