from django.db import models

from messages.fields import BlobField, IMessageTimeStampField

class Message(models.Model):
	class Meta:
		db_table = 'message'

	rowid = models.IntegerField(primary_key=True)
	guid = models.TextField(unique=True)
	text = models.TextField()
	replace = models.IntegerField()
	service_center = models.TextField()
	handle = models.ForeignKey('Handle')
	subject = models.TextField()
	country = models.TextField()
	attributedBody = BlobField()
	version = models.IntegerField()
	type = models.IntegerField()
	service = models.TextField()
	account = models.TextField()
	account_guid = models.TextField()
	error = models.IntegerField()
	date = IMessageTimeStampField()
	date_read = IMessageTimeStampField()
	date_delivered = IMessageTimeStampField()
	is_delivered = models.BooleanField()
	is_finished = models.BooleanField()
	is_emote = models.BooleanField()
	is_from_me = models.BooleanField()
	is_empty = models.BooleanField()
	is_delayed = models.BooleanField()
	is_auto_reply = models.BooleanField()
	is_prepared = models.BooleanField()
	is_read = models.BooleanField()
	is_system_message = models.BooleanField()
	is_sent = models.BooleanField()
	has_dd_results = models.BooleanField()
	is_service_message = models.BooleanField()
	is_forward = models.BooleanField()
	was_downgraded = models.BooleanField()
	is_archive = models.BooleanField()
	cache_has_attachments = models.BooleanField()
	cache_roomnames = models.TextField()
	was_data_detected = models.BooleanField()
	was_deduplicated = models.BooleanField()

class Handle(models.Model):
	class Meta:
		db_table = 'handle'

	rowid = models.IntegerField(primary_key=True)
	id = models.TextField()
	country = models.TextField()
	service = models.TextField()
	uncanonicalized_id = models.TextField()

	def __unicode__(self):
		return self.id
