from django.contrib import admin
from django.utils.html import format_html
from .models import Contact, Project


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'message')
    list_filter = ('message',)


admin.site.register(Contact, ContactAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'preview')
    list_filter = ('name',)


  # list displayga qolgan imagelarni qoshish uchun previewLAR 3 TA YOZILISHI KK, Tepada ham preview 1 ,2 ,3 15- qatorda
    # def preview(self, obj):
    # def preview(self, obj):
    # def preview(self, obj):
    def preview(self, obj):
        html_code = f"""<img src={obj.image1.url} alt="No image" width="50" height="60">"""

        return format_html(html_code)


admin.site.register(Project, ProjectAdmin)
