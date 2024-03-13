from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def non_negative_validator(value):
    if value <= 0:
        raise ValidationError("Будь ласка вкажіть коректну ціну.")

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("name", "user")

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField(validators=[non_negative_validator])
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    class Meta:
        unique_together = ("name", "category")

    def __str__(self):
        return self.name

