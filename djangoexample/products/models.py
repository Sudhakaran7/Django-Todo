from django.db import models

# Create your models here.
class Product(models.Model):
    item=models.CharField(max_length=200,default='')
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' +str(self.completed)