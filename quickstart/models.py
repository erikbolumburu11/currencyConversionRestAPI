from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=3)
    symbol = models.CharField(max_length=1)

    def __str__(self):
        return self.name

# Create your models here.
class Conversion(models.Model):
    from_cur = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="from_currency")
    to_cur = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="to_currency")
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=2)