from django.db import models
from django.urls import reverse

class Item(models.Model):
    description = models.TextField(max_length=250)
    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('items_index', kwargs={'item_id': self.id})

    class Meta:
        ordering = ['id']