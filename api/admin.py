from django.contrib import admin
from .models import Page
# Register your models here.
admin.site.register(Page)
class StudnetAdmin(admin.ModelAdmin):
    list_display = '__all__'