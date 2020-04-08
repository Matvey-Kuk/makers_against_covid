from django.contrib import admin


from . import models

admin.site.register(models.Ticket)
admin.site.register(models.TicketUpdate)
