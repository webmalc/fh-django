from django.contrib import admin

class ModelOptions(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"

class StackedItemInline(admin.StackedInline):
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class TabularItemInline(admin.TabularInline):
    classes = ('grp-collapse grp-open',)
