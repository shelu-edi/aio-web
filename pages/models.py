from django.db import models

# Create your models here.

class Store(models.Model):
    store_name = models.CharField(max_length=1000)
    owner = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='store/img/')

    def __str__(self):
        return self.store_name
