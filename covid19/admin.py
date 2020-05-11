from django.contrib import admin
from.models import *
from import_export.admin import ImportExportModelAdmin


##from.admin import DistrictwiseCovid

# Register your models here.
##admin.site.register(Developer,DistrictwiseCovid)





class DistrictwiseCovidAdmin(ImportExportModelAdmin):
    pass


##admin.site.register(DistrictwiseCovidAdmin)



class DeveloperAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['cname','img','death','positive','quarantine']

admin.site.register(Developer,DeveloperAdmin)
admin.site.register(DistrictwiseCovid,DistrictwiseCovidAdmin)
'''class DeveloperAdmin(ImportExportModelAdmin):
    pass'''







