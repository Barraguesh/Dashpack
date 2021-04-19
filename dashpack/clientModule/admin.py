from django.contrib import admin
from clientModule import models
from rest_framework.authtoken.admin import TokenAdmin

#Modules
admin.site.register(models.Client)
admin.site.register(models.Device)
admin.site.register(models.Ticket)

#API token generator
TokenAdmin.raw_id_fields = ['user']