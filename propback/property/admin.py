from django.contrib import admin
from .models import Property, MyTags, PropsImage

# Register your models here.

class PropsImageAdmin(admin.StackedInline):
    model = PropsImage
    
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines =[PropsImageAdmin]

    class Meta:
        model = Property
        

@admin.register(PropsImage)
class PropsImageAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Property)
#admin.site.register(MyTags)
#admin.site.register(PropsImage)
