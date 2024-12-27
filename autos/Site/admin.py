from django.contrib import admin
from .models import Vehicle, Img, Description


class AutoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'anio', 'precio')
    search_fields = ('marca', 'modelo')
admin.site.register(Vehicle,AutoAdmin)    

class ImgAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'url')
    search_fields = ('vehicle', 'url')
admin.site.register(Img, ImgAdmin)    

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'title')
    search_fields = ('vehicle', 'title')
admin.site.register(Description, DescriptionAdmin)
