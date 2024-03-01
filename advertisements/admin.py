from django.contrib import admin

from advertisements.models import AdvertisementStatusChoices, Advertisement

# Register your models here.
admin.site.register(Advertisement)
# admin.site.register(AdvertisementStatusChoices)
