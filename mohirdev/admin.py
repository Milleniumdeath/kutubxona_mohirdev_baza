from django.contrib import admin
from .models import *
admin.site.register(
    [Profile, Kurs, Izoh, Tanlangan, Xarid,]
)
