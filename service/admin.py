from django.contrib import admin
from service.models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('icon','name','title')
    
admin.site.register(Service,ServiceAdmin)
