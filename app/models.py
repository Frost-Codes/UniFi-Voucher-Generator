from django.db import models

# Create your models here.


class Image(models.Model):
    image_description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image_description

