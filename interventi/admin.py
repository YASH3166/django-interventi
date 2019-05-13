from django.contrib import admin
from django.contrib.auth.models import User

from .models import (
    Fornitore, PuntoVendita,
)


class FornitoreAdmin(admin.ModelAdmin):
    """
    Custom Fornitore admin class
    """
    list_display = (
        'nome', 'tipo_servizio_offerto', 'citta', 'referente', 'email', 'telefono',
    )
    ordering = (
        'nome',
    )
    list_filter = (
        'citta', 'referente',
    )
    search_fields = (
        'nome', 'citta', 'referente',
    )


class PuntoVenditaAdmin(admin.ModelAdmin):
    """
    Custom PuntoVendita admin class
    """
    list_display = (
        'nome', 'citta', 'responsabile', 'email', 'telefono',
    )
    ordering = (
        'nome',
    )
    list_filter = (
        'citta', 'responsabile',
    )
    search_fields = (
        'nome', 'citta', 'responsabile',
    )


class FornitoreInline(admin.TabularInline):
    model = Fornitore
    # can_delete = True
    verbose_name_plural = 'fornitori'


admin.site.register(Fornitore, FornitoreAdmin)
admin.site.register(PuntoVendita, PuntoVenditaAdmin)
