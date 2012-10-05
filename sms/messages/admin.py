from messages.models import Message
from django.contrib import admin


class MessageAdmin(admin.ModelAdmin):
	list_display = ('date', 'service', 'handle_id', 'account', 'text')

admin.site.register(Message, MessageAdmin)
