from django.db import models

class SatellitePart(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    part_number = models.CharField(max_length=50, unique=True, verbose_name="S/N")
    manufacturer = models.CharField(max_length=100, verbose_name="manufacturer")
    description = models.CharField(blank=True, verbose_name="desription")
    quantity = models.PositiveIntegerField(default=0, verbose_name="quantity")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.part_number} - {self.name}"
   
    class Meta:
        verbose_name = "spare part"
        verbose_name_plural = "spare parts"
# Create your models here.
