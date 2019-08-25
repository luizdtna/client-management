from django.contrib import admin
from .models import Pessoa, Document, Sale, Product

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Document)
admin.site.register(Sale)
admin.site.register(Product)