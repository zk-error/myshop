from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    valid_from = models.DateTimeField()#fecha y hora inicio de cupon 
    valid_to = models.DateTimeField()#fecha y hora final del cupon
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],help_text='Percentage vaule (0 to 100)')
    active = models.BooleanField()

    def __str__(self):
        return self.code