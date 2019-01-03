import quandl

quandl.ApiConfig.api_key = "EDyLzB9sdbNDQyXm_NhG"

data = quandl.get_table('ZACKS/P', ticker='MSFT', paginate=True)

print(data)