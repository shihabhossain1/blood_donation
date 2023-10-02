from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    exprire_date = models.DateField(blank=True, null=True)

    image = models.FileField(upload_to='product/image', blank=True, null=True)

    description = models.TextField()

    stock = models.BooleanField(default=True)

    added_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.name} / {self.price} tk./ {self.exprire_date} /{self.added_on}"