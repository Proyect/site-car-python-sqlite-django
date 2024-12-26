from django.contrib import admin
from .models import Vehicle, Img, Description


class AutoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'anio', 'precio')
    search_fields = ('marca', 'modelo')
admin.site.register(Vehicle,AutoAdmin)    

class ImgAdmin(admin.ModelAdmin):
    list_display = ('id_vehicle', 'url')
    search_fields = ('id_vehicle', 'url')
admin.site.register(Img, ImgAdmin)    

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('id_vehicle', 'title')
    search_fields = ('id_vehicle', 'title')
admin.site.register(Description, DescriptionAdmin)
