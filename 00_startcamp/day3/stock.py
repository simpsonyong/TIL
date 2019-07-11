from iexfinance.stocks import Stock
import random

companies = ['AAPL', 'GOOGL', 'TSLA', 'FB', 'AMZN']
company = Stock(random.choice(companies), token='pk_63c229409ff14b67a6cc81e38927f1c4')

print(company.get_quote())
