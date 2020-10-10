from alfa_cv import AlfaCV
from parser_message import ParserMessage
from db import Message

def create_message_with_file(file):
	a = AlfaCV(file)
	messages = a.get_messages()

	bulk_list = []
	for message in messages:
		parser = ParserMessage(message)

		bulk_list.append(Message(
			card= parser.get_card(),
			balance = parser.get_balance(),
			amount = parser.get_amount(),
			currency = parser.get_currency(),
			date=  parser.get_date(),
			body=parser.text
			))

	Message.bulk_create(bulk_list)