from django.contrib import admin
from people.models import Person, Biography


class PersonBioInline(admin.TabularInline):
    model = Biography
    extra = 0


class PersonAdmin(admin.ModelAdmin):
    inlines = [PersonBioInline]
    exclude = ('biography',)

admin.site.register(Person, PersonAdmin)
admin.site.register(Biography)
