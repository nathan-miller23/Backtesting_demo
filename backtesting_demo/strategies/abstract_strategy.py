class Abstract_strategy:

	NAME = ''

	def __init__(self, data, ticker, days):
		self.data = data
		self.ticker = ticker
		self.days = days

	def apply():
		# 'Abstract' method to be implemented by child classes
		self.val = 0.0

	def __str__(self):
		# Print calculated value in standard formatted manner
		return 'The ' + str(self.days) + ' day ' + self.NAME + ' for ' + self.ticker + ' is ' + str(round(self.val, 3)) + '\n'