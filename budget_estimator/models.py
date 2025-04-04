from django.db import models

class InteriorDesign(models.Model):
    component = models.CharField(max_length=100)
    modern_price = models.IntegerField()
    classic_price = models.IntegerField()
    minimalist_price = models.IntegerField()
    bohemian_price = models.IntegerField()

    def __str__(self):
        return self.component