from django.contrib import admin
from .models import Service, ServiceImage


#Register Services and images service django admin
class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceImageInline]

admin.site.register(ServiceImage)



