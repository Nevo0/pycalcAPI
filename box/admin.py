from django.contrib import admin
from .models import Box, MaxHubsSideAB, MaxHubsSideCD, Termina, Certificate, MaximumPowerDissipation, Order

# Register your models here.
admin.site.register(Order)
admin.site.register(Box)
admin.site.register(MaxHubsSideAB)
admin.site.register(MaxHubsSideCD)
admin.site.register(Termina)
admin.site.register(Certificate)
admin.site.register(MaximumPowerDissipation)
