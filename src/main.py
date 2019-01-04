import quandl
import sys
from strategies.simple_moving_average import Simple_moving_average

API_KEY = "EDyLzB9sdbNDQyXm_NhG"
quandl.ApiConfig.api_key = "EDyLzB9sdbNDQyXm_NhG"
data = quandl.get_table('ZACKS/P', ticker='MSFT', paginate=True)

ticker = sys.argv[1]
days = sys.argv[2]

strategies = [Simple_moving_average]

for strat in strategies:
	s = strat(quandl, ticker, days)
	s.apply()
