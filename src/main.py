import quandl
import sys
from strategies.simple_moving_average import Simple_moving_average
from strategies.exponential_moving_average import Exponential_moving_average
from strategies.volume_weighted_moving_average import Volume_weighted_moving_average

# Authenticate quandl instance
API_KEY = "EDyLzB9sdbNDQyXm_NhG"
quandl.ApiConfig.api_key = "EDyLzB9sdbNDQyXm_NhG"

# Scrape commandline arguments
ticker = sys.argv[1]
days = int(sys.argv[2])

# Check for valid input
assert days > 0, 'Days argument ' + str(days) + ' is invalid. Please enter a positive integer'

# Hit quandl api to get all prices for given ticker
data = quandl.get_table('ZACKS/P', ticker=ticker, paginate=True)

# Check for valid input
assert not data.empty, 'Ticker argument ' + str(ticker) + ' is invalid. Please enter a valid ticker'

# List of each backtesting strategy we would like to apply
strategies = [Simple_moving_average, Exponential_moving_average, Volume_weighted_moving_average]

# Iteratively apply each strategy 
for strat in strategies:
	s = strat(data, ticker, days)
	s.apply()
