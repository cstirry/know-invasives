from django.db import models

# Create your models here.
class Plant(models.Model):
    common_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    synonym = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)  # 'habit' in the Excel file
    invasive = models.BooleanField(default=False)
    symbol = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.common_name
