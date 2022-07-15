from django.contrib import admin

from .models import meetup, Location, Participant

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display=('title', 'date', 'location', )
    list_filter=('location', 'date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)