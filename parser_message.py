import re
from datetime import datetime

class ParserMessage:
	date_formate = "%d.%m.%y %H:%M"
	date_formate_re = "\d{2}.\d{2}.\d{2}\s\d{2}:\d{2}"
	CURRENCY = ("UAH",'USD')
	
	def __init__(self,text):
		# clear artifakts
		self.text = text.replace("\n\n","").replace('\n \n',"").replace('\nA ',"")
		print(self.text)
	def get_currency(self):
		for currency in self.CURRENCY:
			if currency in self.text:
				return currency

	def get_balance(self):
		text = re.search('Dostupno.[\s\d.]+\w+', self.text)
		text = text.group() if text else None
		if text:
			amount = re.search('[\s\d.]+',text).group()
			if amount: 
				return float(amount)

	def get_amount(self):
		text = re.search('[+-][\d.]+\w+', self.text)
		text = text.group() if text else None
		if text:
			amount = re.search('[+-][\d.]+', text).group()
			if amount:
				return float(amount)

	def get_card(self):
		return re.search('[\d*]{11}', self.text).group()

	def get_date(self):
		date_str = re.search(self.date_formate_re, self.text).group()
		return datetime.strptime(date_str, self.date_formate )

# def testParserMessage():
	# p = ParserMessage(''' 
	# A Alfa-Bank

	 

	# Kartka 5355***9589 uspishna operaciya
	# +21550.00UAH 08.10.20 13:26 Concord A2C, UA
	# Dostupno:26881.84UAH
	# ''')
	# print("card",p.get_card())
	# print("amount",p.get_amount())
	# print("balance",p.get_balance())
	# print("date",p.get_date())
	# print("text",p.text)
	# M = p.get_message()
	# print("Message",M)
	# print(dir(M))