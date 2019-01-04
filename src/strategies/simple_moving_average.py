 from strategies.abstract_strategy import Abstract_strategy

class Simple_moving_average(Abstract_strategy):

	NAME = 'Simple moving average'

	def __init__(self, quandl, ticker, days):
		# Call parent class constructor to set instance variables
		super().__init__(quandl, ticker, days)

	def apply(self):
		# Make API call here
		data = self.quandl.get_table('ZACKS/P', ticker=self.ticker, paginate=True)

		# Select closing price over the last @param days days 
		data = data['close'][-1*self.days:]

		# Calculate the SMA
		self.val = sum(data) / self.days

		# Print calculated value 
		self.to_string()

