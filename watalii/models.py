from django.db import models

# Create your models here.
class Destination(models.Model):
    image = models.ImageField(upload_to="img/")
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name