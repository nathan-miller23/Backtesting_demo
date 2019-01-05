class Abstract_strategy:

	NAME = ''

	def __init__(self, data, ticker, days):
		self.data = data
		self.ticker = ticker
		self.days = days

	def apply():
		# 'Abstract' method to be implemented by child classes
		self.val = 0.0

	def to_string(self):
		# Print calculated value in standard formatted manner
		print('The ' + str(self.days) + ' day ' + self.NAME + ' for ' + self.ticker + ' is ' + str(round(self.val, 3)) + '\n')