from strategies.abstract_strategy import Abstract_strategy

class Volume_weighted_moving_average(Abstract_strategy):

	NAME = 'Volume Weighted moving average'

	def __init__(self, data, ticker, days):
		# Call parent class constructor to set instance variables
		super().__init__(data, ticker, days)

	def apply(self):

		# helper function to find average
		def f(a, b, c):
			return (a + b + c) / 3

		# Splice data for only days we're interested in
		self.data = self.data[-1*self.days:].copy()

		# This is to avoid all NaNs on sundays by replacing them with 0s
		self.data.fillna(0, inplace=True)

		# Create new column with the average of 'high', 'low', and 'close' called 'typical price'
		self.data['typical price'] = self.data[['high', 'low', 'close']].apply(lambda x : f(*x), axis=1)

		# Create new column called 'weighted price' that is the product of 'volume' and 'typical price'
		self.data['weighted price'] = self.data[['typical price', 'volume']].apply(lambda x : x[0]*x[1], axis=1)

		# Sum over 'volume' col to get total number transactions during period
		total_volume = sum(self.data['volume'])

		# Execute VWAP formula
		self.val = sum(self.data['weighted price']) / total_volume

		# Print with formatting
		print(self)

