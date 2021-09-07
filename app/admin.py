from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from .models import Profile, Mold, Manufacturer, Product, Category, Mold_type, Piece_id, PropertyImage
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from mptt.admin import MPTTModelAdmin, TreeRelatedFieldListFilter, DraggableMPTTAdmin



admin.site.site_header= " توانکار "
admin.site.site_title= "Tavankar"
admin.site.register(LogEntry)





#------------------------------------------------------------------------------
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('user_name','phone','address')
    search_fields = ['user_name', 'phone', 'address']

admin.site.register(models.Profile, ProfileAdmin)



#------------------------------------------------------------------------------
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class MoldAdmin(ImportExportModelAdmin):
    list_display = ('Name','Code','Type','Cavities_qty','image_tag','Year')
    list_filter = ("Type", "Cavities_qty")
    search_fields = ['Name', 'Code']
    raw_id_fields = ('Category',)
    inlines = [ PropertyImageInline, ]

    '''
    fields = (
        ('Name', 'Code'),
        ('Type', 'Manufacturer', 'Material'),
        ('Piece_id', 'Cavities_id'),
        ('Cavities_qty', 'Healthy_Cavities_qty', 'Mold_qty'),
        ('Related_product', 'Category'),
        ('Image', 'File'),
        ('Address', 'Year'),
        'Description'
        )
    '''

admin.site.register(models.Mold, MoldAdmin)




#------------------------------------------------------------------------------
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('Name','short_description','image_tag')
    search_fields = ['Name', 'short_description']

admin.site.register(models.Product, ProductAdmin)





#------------------------------------------------------------------------------
class ManufacturerAdmin(ImportExportModelAdmin):
    list_display = ('Name','short_description')
    search_fields = ['Name', 'short_description']

admin.site.register(models.Manufacturer, ManufacturerAdmin)




#------------------------------------------------------------------------------
class Mold_typeAdmin(ImportExportModelAdmin):
    list_display = ('Name','Name')
admin.site.register(models.Mold_type, Mold_typeAdmin)



#------------------------------------------------------------------------------
class Piece_idAdmin(ImportExportModelAdmin):
    list_display = ('Name','Name')
admin.site.register(models.Piece_id, Piece_idAdmin)




#------------------------------------------------------------------------------
class CategoryMPTTModelAdmin(ImportExportMixin, MPTTModelAdmin, TreeRelatedFieldListFilter):
    mptt_level_indent = 15

admin.site.register(Category, DraggableMPTTAdmin,
    list_display=('tree_actions', 'indented_title'),
    list_display_links=('indented_title',),)














#-------------------------------------------------------- by Nima Dorostkar ---
