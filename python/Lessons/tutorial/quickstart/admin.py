from django.contrib import admin
from .models import Car, Transmission
from django.utils.translation import gettext_lazy as _
from django.urls import path


class CarAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Car info'), {'fields': (
            'name',
        )}),
        (_('Spec'), {'fields': (
            'max_speed',
            'engine_type',
        )}),
        (_('Transmission spec'), {'fields': (
            'transmission',
        )}),
    )

    list_filter = ('max_speed', 'engine_type')
    list_display = (
        'name',
        'max_speed',
        'engine_type',
        'transmission'
    )

    ordering = ('max_speed', 'name', )
    search_fields = ('max_speed', 'name', 'engine_type',)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                'testapp/car/',
                self.admin_site.admin_view(self.multiple_action),
                name='some-action',
            ),
        ]
        return my_urls + urls

    def multiple_action(self, request, queryset):
        print(f'__request:{request}________queryset:_{queryset}___')

    multiple_action.short_description = 'Some action'
    actions = ['multiple_action', ]


# Register your models here.
# admin.site.register([Car, Transmission])
admin.site.register(Car, CarAdmin)
admin.site.register(Transmission)
