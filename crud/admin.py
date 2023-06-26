from django.contrib import admin
from .models import MascotType, Mascot, Vaccine

# Register your models here.
class VaccineAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','vaccine')
    ordering = ('vaccine',)

class MascotTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','mascotType')
    ordering = ('mascotType',)

class MascotAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('idMascot','name','mascotType','breed')
    ordering = ('name',)

admin.site.register(MascotType,MascotTypeAdmin)
admin.site.register(Mascot,MascotAdmin)
admin.site.register(Vaccine,VaccineAdmin)