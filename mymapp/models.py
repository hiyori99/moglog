# mymapp/models.py

from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    visit_count = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Menu(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True, default='')
    menu = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


