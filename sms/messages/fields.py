from django.conf import settings
from django.db import models

from datetime import datetime
from pytz import timezone
from time import mktime

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
			return datetime.fromtimestamp(value+self.IMESSAGE_DELTA).replace(tzinfo=app_tz)
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

