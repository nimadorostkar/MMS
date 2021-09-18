from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from .models import Profile, Mold, Manufacturer, Product, Category, Mold_type, Piece_id, MoldImage, Repair_request, RepairImage, Repair_operation, OperationImage, Manufacture_request, Component_request, ComponentImage
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from mptt.admin import MPTTModelAdmin, TreeRelatedFieldListFilter, DraggableMPTTAdmin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin


admin.site.site_header= " توانکار "
admin.site.site_title= "Tavankar"
admin.site.register(LogEntry)



#------------------------------------------------------------------------------
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('user_name','phone','address')
    search_fields = ['user_name', 'phone', 'address']

admin.site.register(models.Profile, ProfileAdmin)





#------------------------------------------------------------------------------
class MoldImageInline(admin.TabularInline):
    model = MoldImage
    extra = 1

class MoldAdmin(ImportExportModelAdmin):
    list_display = ('Name','Code','Type','Cavities_qty','Year')
    list_filter = ("Type", "Cavities_qty")
    search_fields = ['Name', 'Code']
    raw_id_fields = ('Category', 'Type', 'Piece_id', 'Manufacturer')
    inlines = [ MoldImageInline, ]

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
    search_fields = ['Name']
admin.site.register(models.Mold_type, Mold_typeAdmin)





#------------------------------------------------------------------------------
class Piece_idAdmin(ImportExportModelAdmin):
    list_display = ('Name','Name')
    search_fields = ['Name']
admin.site.register(models.Piece_id, Piece_idAdmin)





#------------------------------------------------------------------------------
class CategoryMPTTModelAdmin(ImportExportMixin, MPTTModelAdmin, TreeRelatedFieldListFilter):
    mptt_level_indent = 15

admin.site.register(Category, DraggableMPTTAdmin,
    list_display=('tree_actions', 'indented_title'),
    list_display_links=('indented_title',),)






#------------------------------------------------------------------------------
class OperationImageInline(admin.TabularInline):
    model = OperationImage
    extra = 1

class Repair_operationAdmin(ImportExportModelAdmin):
    list_display = ('Step','Request','short_description')
    list_filter = ("Step", "Request")
    search_fields = ['Request','short_description']
    inlines = [ OperationImageInline, ]

admin.site.register(models.Repair_operation, Repair_operationAdmin)






#------------------------------------------------------------------------------
class RepairImageInline(admin.TabularInline):
    model = RepairImage
    extra = 1

class Repair_requestAdmin(ModelAdminJalaliMixin,ImportExportModelAdmin):
    list_display = ('Mold','Applicant')
    list_filter = ("Mold", "Applicant")
    search_fields = ['Mold', 'Applicant']
    raw_id_fields = ('Mold',)
    inlines = [ RepairImageInline, ]

admin.site.register(models.Repair_request, Repair_requestAdmin)





#------------------------------------------------------------------------------
class Manufacture_requestAdmin(ModelAdminJalaliMixin,ImportExportModelAdmin):
    list_display = ('Mold','Status') 

admin.site.register(models.Manufacture_request, Manufacture_requestAdmin)





#------------------------------------------------------------------------------
class ComponentImageImageInline(admin.TabularInline):
    model = ComponentImage
    extra = 1

class Component_requestAdmin(ModelAdminJalaliMixin,ImportExportModelAdmin):
    list_display = ('short_description','Applicant','Status')
    inlines = [ ComponentImageImageInline, ]

admin.site.register(models.Component_request, Component_requestAdmin)










#-------------------------------------------------------- by Nima Dorostkar ---
