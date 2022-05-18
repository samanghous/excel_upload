from django.db import models

class ExcelData(models.Model):
    name = models.CharField(max_length = 100,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    hobby = models.CharField(max_length = 100,null=True,blank=True)
    date_created = models.DateField(null=True,blank=True)

    def __str___(self):
        return self.name 
