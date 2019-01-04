class Abstract_strategy:

	NAME = ''

	def __init__(self, quandl, ticker, days):
		self.quandl = quandl
		self.ticker = ticker
		self.days = days

	def apply():
		self.val = 0.0

	def to_string(self):
		print('The ' + self.days + ' day ' + self.NAME + ' for ' + self.ticker + ' is ' + str(self.val) + '\n')