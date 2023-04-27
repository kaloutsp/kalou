from django.db import models

#IMPORT_URL = https://cloudonapi.oncloud.gr/s1services/JS/updateItems/cloudOnTest
# Create your models here.

class TableData(models.Model):
    externalId = models.IntegerField(max_length=200, unique=True)
    code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=200,blank=True, null=True)
    barcode = models.IntegerField(blank=True, null=True)
    retailPrice = models.PositiveIntegerField(blank=True, null=True)
    wholesalePrice = models.PositiveIntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
