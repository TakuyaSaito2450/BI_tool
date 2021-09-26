from django.contrib import admin
from .models import ExcelModel, Prefectures, Littering
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class ExcelModelAdmin(ImportExportModelAdmin):
    class ExcelResources(resources.ModelResource):
        class Meta:
            model = ExcelModel
            skip_unchanged = True
            report_skipped = False
            import_id_fields = ('name', )

    resource_class = ExcelResources


class PrefecturesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


class LitteringAdmin(admin.ModelAdmin):
    list_display = ('prefectures', 'collection_date')
    list_display_links = ('prefectures',)


admin.site.register(ExcelModel, ExcelModelAdmin)
admin.site.register(Prefectures)
admin.site.register(Littering)

