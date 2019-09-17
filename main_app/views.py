from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Item

class ItemList(ListView):
    model = Item

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'

class ItemDelete(DeleteView):
    model = Item
    success_url = '/'

class ItemUpdate(UpdateView):
  model = Item
  fields = ['description']
  success_url = '/'
