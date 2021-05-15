from django.contrib import admin

# Register your models here.
from anime.models import Bangumi, StorageInfo

admin.site.register(Bangumi)
admin.site.register(StorageInfo)
