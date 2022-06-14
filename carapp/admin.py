from django.contrib import admin
from carapp import models

# Register your models here.

class caradmin(admin.ModelAdmin):
    model=models.car
    display=[
        "model_name",
        "model_number",
        "model_prize"
    ]

class owneradmin(admin.ModelAdmin):
    model=models.owner
    display=[
        "owner_name",
        "owner_mobile"
    ]

class orderadmin(admin.ModelAdmin):
    model=models.order
    display=[
        "owner",
        "car",
        "unit"
    ]

admin.site.register(models.car,caradmin)
admin.site.register(models.owner,owneradmin)
admin.site.register(models.order,orderadmin)    