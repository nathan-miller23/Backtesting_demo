import quandl
import sys
from strategies.simple_moving_average import Simple_moving_average
from strategies.exponential_moving_average import Exponential_moving_average
from strategies.volume_weighted_moving_average import Volume_weighted_moving_average

API_KEY = "EDyLzB9sdbNDQyXm_NhG"
quandl.ApiConfig.api_key = "EDyLzB9sdbNDQyXm_NhG"

ticker = sys.argv[1]
days = int(sys.argv[2])
data = quandl.get_table('ZACKS/P', ticker=ticker, paginate=True)

strategies = [Simple_moving_average, Exponential_moving_average, Volume_weighted_moving_average]

for strat in strategies:
	s = strat(data, ticker, days)
	s.apply()
