from strategies.abstract_strategy import Abstract_strategy

class Exponential_moving_average(Abstract_strategy):

	NAME = 'Exponential moving average'

	def __init__(self, data, ticker, days):
		# Call parent class constructor to set instance variables
		super().__init__(data, ticker, days)

	def apply(self):

		# Select closing price over the last @param days days 
		closing_prices = self.data['close'][-1*self.days:]

		# Calculate the weighting multiplier
		multiplier = 2 / (self.days + 1)

		# Recursively calculate the EMA (curr_day - 1) days ago 
		def helper(curr_day):
			if curr_day == self.days:
				# Use the current price as a base case
				return closing_prices.iloc[-1*curr_day]
			else:
				# Follow recursive formula for EMA
				return multiplier*closing_prices.iloc[-1*curr_day] + (1 - multiplier) * helper(curr_day + 1)

		self.val = helper(1)

		# Print calculated value 
		self.to_string()

