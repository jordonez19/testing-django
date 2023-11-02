from django.db import models
# Create your models here.
class Customer(models.Model):
    name  = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    logo = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name