from django.contrib import admin
from .models import FileUploadModel, ImageUploadModel
# Register your models here.

class FileUploadModelAdmin(admin.ModelAdmin):
    def get_file_url(self, obj):
        return obj.uploaded_file.url

    date_hierarchy = 'uploaded_on'

    list_display = ('id','purpose', 'user', 'get_file_url', 'uploaded_on')
    list_filter = ('purpose','user__username')

    search_fields = ('id', 'purpose', 'user__username')

admin.site.register(FileUploadModel, FileUploadModelAdmin)

class ImageUploadModelAdmin(admin.ModelAdmin):
    def get_image_url(self, obj):
        return obj.uploaded_image.url

    date_hierarchy = 'uploaded_on'

    list_display = ('id','purpose', 'user', 'get_image_url', 'uploaded_on')
    list_filter = ('purpose','user__username')

    search_fields = ('id', 'purpose', 'user__username')

admin.site.register(ImageUploadModel,ImageUploadModelAdmin)