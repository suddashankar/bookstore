from django.contrib import admin
from bookapp.models import Category,Book
models=[Category,Book]
admin.site.register(models)
