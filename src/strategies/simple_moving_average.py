from strategies.abstract_strategy import Abstract_strategy

class Simple_moving_average(Abstract_strategy):

	NAME = 'Simple moving average'

	def __init__(self, data, ticker, days):
		# Call parent class constructor to set instance variables
		super().__init__(data, ticker, days)

	def apply(self):

		# Select closing price over the last @param days days 
		closing_prices = self.data['close'][-1*self.days:]

		# Calculate the SMA
		self.val = sum(closing_prices) / self.days

		# Print calculated value 
		self.to_string()

