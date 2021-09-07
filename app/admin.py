from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from .models import Profile, Mold
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin



admin.site.site_header= " توانکار "
admin.site.site_title= "Tavankar"
admin.site.register(LogEntry)





#------------------------------------------------------------------------------
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('user_name','phone','address')
    search_fields = ['user_name', 'phone', 'address']

admin.site.register(models.Profile, ProfileAdmin)




#------------------------------------------------------------------------------
class MoldAdmin(ImportExportModelAdmin):
    list_display = ('Name','Code','Type','Cavities_qty','image_tag','Year')
    list_filter = ("Type", "Cavities_qty")
    search_fields = ['Name', 'Code']

admin.site.register(models.Mold, MoldAdmin)
















#-------------------------------------------------------- by Nima Dorostkar ---
