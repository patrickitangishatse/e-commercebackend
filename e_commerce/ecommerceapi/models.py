from django.db import models



# Product model starts

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=50)
    # image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    

# Product models ends