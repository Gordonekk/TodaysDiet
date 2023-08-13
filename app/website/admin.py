from django.contrib import admin
from website.models import Food

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind')

admin.site.register(Food, FoodAdmin)
