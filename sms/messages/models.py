from django.db import models
from django.conf import settings
from datetime import datetime
from time import mktime
from pytz import timezone

class BlobField(models.Field):

	description = "A Sqlite3 BLOB field wrapper."

	def db_type(self, connection):
		return 'blob'
		

class IMessageTimeStampField(models.DateTimeField):
	description = "iMessage timestamp field where epoch=1/1/2001"

	# Delta between 1/1/2001 and unix epoch
	IMESSAGE_DELTA = 978307200

	__metaclass__ = models.SubfieldBase

	def __init__(self, null=False, blank=False, **kwargs):
		super(IMessageTimeStampField, self).__init__(**kwargs)

	def db_type(self, connection):
		return 'int'

	def to_python(self, value):
		super(IMessageTimeStampField, self)
		try:
			app_tz = timezone(settings.TIME_ZONE)
			return datetime.fromtimestamp(value+IMessageTimeStampField).replace(tzinfo=app_tz)
		except:
			return value


	def get_db_prep_value(self, value):
		if value==None:
			return None
		return mktime(value.timetuple())

	def get_prep_value(self, value):
		if value==None:
			return None
		return mktime(value.timetuple())

class Message(models.Model):
	class Meta:
		db_table = 'message'

	rowid = models.IntegerField(primary_key=True)
	guid = models.TextField(unique=True)
	text = models.TextField()
	replace = models.IntegerField()
	service_center = models.TextField()
	handle_id = models.IntegerField()
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
