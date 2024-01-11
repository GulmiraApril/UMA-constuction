from django.contrib import admin
from django.utils.html import format_html
from .models import AboutCompany, Contact, Project, MainPage


class AboutCompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title',)


admin.site.register(AboutCompany, AboutCompanyAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'message')
    list_filter = ('message', )


admin.site.register(Contact, ContactAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'description', 'preview')
    list_filter = ('project_name',)

    def preview(self, obj):
        html_code = f"""<img src={obj.project_image.url} alt="No image" width="50" height="60">"""

        return format_html(html_code)


admin.site.register(Project, ProjectAdmin)


class MainAdmin(admin.ModelAdmin):
    list_display = ('moto', 'main_image', 'preview')
    list_filter = ('moto',)

    def preview(self, obj):
        html_code = f"""<img src={obj.main_image.url} alt="No image" width="50" height="60">"""

        return format_html(html_code)


admin.site.register(MainPage, MainAdmin)
