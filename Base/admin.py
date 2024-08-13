from django.contrib import admin

from Base.models import Uploadfile

# Register your models here.
@admin.register(Uploadfile)
class UploadfileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
