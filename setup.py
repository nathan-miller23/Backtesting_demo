from setuptools import setup

setup(
   name='backtesting_demo',
   version='1.0',
   description='Module for applying various backtesting strategies to tickers of choice',
   author='Nathan Miller',
   author_email='nathan_miller23@berkeley.edu',
   packages=['backtesting_demo'],  #same as name
   install_requires=['quandl'], #external packages as dependencies
)