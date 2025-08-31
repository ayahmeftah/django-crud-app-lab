from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'owner'

    def __str__(self):
        return self.name
    
class Electronic(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="electronics")

    class Meta:
        db_table = 'electronic'

    def __str__(self):
        return f"{self.name} ({self.type})"