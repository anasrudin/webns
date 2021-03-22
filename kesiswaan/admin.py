from django.contrib import admin
from .forms import KehadiranSiswaForm

# Register your models here.

# from .forms import KehadiranSiswaForm

class KehadiranSiswaAdmin(admin.ModelAdmin):
    raw_id_fields = ['datasiswa']
    list_display = ["status", "catatan"]
    form = KehadiranSiswaForm