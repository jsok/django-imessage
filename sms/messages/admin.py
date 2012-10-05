from messages.models import Message, Handle
from django.contrib import admin


class MessageAdmin(admin.ModelAdmin):
	list_display = ('date', 'service', 'handle', 'account', 'text')

class HandleAdmin(admin.ModelAdmin):
	list_display = ('id', 'country', 'service')

admin.site.register(Message, MessageAdmin)
admin.site.register(Handle, HandleAdmin)
