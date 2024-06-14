from django.contrib import admin
from .models import Shipment

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname",)
admin.site.register(Shipment,MemberAdmin)
