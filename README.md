# Backtesting_demo

A simple module that calculates various moving averages for a given stock over given time period

### Installation 

Fork this repository and cd to project root. Run 
```
python3 setup.py install
```

### Use

```
python3 backtesting_demo <ticker> <days>
```

### Example

Running something like 
```
python3 backtesting_demo AAPL 10
```
would print out something like
```
The 10 day Simple moving average for AAPL is 152.953

The 10 day Exponential moving average for AAPL is 152.642

The 10 day Volume Weighted moving average for AAPL is 151.891
```