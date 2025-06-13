from django.contrib import admin
from .models import List


class ListingAdmin(admin.ModelAdmin):
    pass

admin.site.register(List)
# Register your models here.
