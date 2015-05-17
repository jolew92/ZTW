from django.contrib import admin
from people.models import Person, Biography


class PersonBioInline(admin.TabularInline):
    model = Biography
    extra = 0


class PersonAdmin(admin.ModelAdmin):
    list_display = "last_name", "first_name", "birthday"
    inlines = [PersonBioInline]
    search_fields = ["first_name", "last_name"]
    exclude = ('biography',)

admin.site.register(Person, PersonAdmin)
admin.site.register(Biography)
