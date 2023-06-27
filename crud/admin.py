from django.contrib import admin
from .models import *

# Register your models here.
class GenderAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','gender')
    ordering = ('gender',)

class MascotTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','mascotType')
    ordering = ('mascotType',)

class MascotAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('idMascot','name','mascotType','breed','gender')
    ordering = ('name',)

admin.site.register(Gender,GenderAdmin)
admin.site.register(MascotType,MascotTypeAdmin)
admin.site.register(Mascot,MascotAdmin)