import pandas as pd 
from strategies.abstract_strategy import Abstract_strategy

class Simple_moving_average(Abstract_strategy):

	NAME = 'Simple moving average'

	def __init__(self, quandl, ticker, days):
		super(Simple_moving_average, self).__init__(quandl, ticker, days)

	def apply(self):
		# Make API call here
		self.val = 10.0
		self.to_string()

