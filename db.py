import peewee# import Model, SqliteDatabase
from datetime import datetime

dbhandle = peewee.SqliteDatabase('db.sqlite')

class Tag(peewee.Model):
	name = peewee.CharField(null=True)
	class Meta:
		database = dbhandle

class Message(peewee.Model):
	card = peewee.CharField(null=True)
	
	body = peewee.TextField()

	balance = peewee.FloatField(null=True)
	amount = peewee.FloatField(null=True)

	currency = peewee.CharField(null=True)
	
	date = peewee.DateTimeField(default=datetime.now())
	def __str__(self):
		return text
	class Meta:
		database = dbhandle
		table_name = 'Message'

class MessageToTag(peewee. Model):
	"""A simple "through" table for many-to-many relationship."""
	tag = peewee.ForeignKeyField(Tag)
	message = peewee.ForeignKeyField(Message)

	class Meta:
		database = dbhandle
		primary_key =  peewee.CompositeKey('tag', 'message')

if __name__ == '__main__':
	try:
		Tag.create_table()
		Message.create_table()
		MessageToTag.create_table()
	except peewee.InternalError as px:
		conn.close()