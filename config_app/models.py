from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_image', null=True, blank=True)
    description = models.TextField()
    price = models.IntegerField()


    def __str__(self):
        return self.name

