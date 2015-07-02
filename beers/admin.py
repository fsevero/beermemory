from django.contrib import admin

# Register your models here.
from .models import BeerType, Brewery, Beer

admin.site.register(BeerType)
admin.site.register(Brewery)
admin.site.register(Beer)
