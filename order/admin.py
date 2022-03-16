from django.contrib import admin

from .models import Order ,Product ,Component, Gladns,Gladn ,Brand,Purchaser, Terminal, Terminals,Additional,SizeGladn,SizeTerminal,TypeTerminal

# Register your models here.

admin.site.register(Order)
admin.site.register(Purchaser)
admin.site.register(Product)
admin.site.register(Component)
admin.site.register(Gladns)
admin.site.register(Gladn)
admin.site.register(Terminal)
admin.site.register(Terminals)
admin.site.register(Additional)
admin.site.register(Brand)
admin.site.register(SizeGladn)
admin.site.register(SizeTerminal)
admin.site.register(TypeTerminal)
