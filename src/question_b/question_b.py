#write functions here, don't add input('') statements here!

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def symbol(self):
        return self.__symbol
    
    def company_name(self):
        return self.__company_name      
    
def stock_purchase_history():
    stock1 = Stock("AAPL", "Apple Inc.")
    stock2 = Stock("CAT", "Caterpillar")
    stock3 = Stock("EK", "Eastman Kodak")
    stock4 = Stock("GOOG", "Google")
    stock5 = Stock("MSFT", "Microsoft")

    stocks = {
        stock1.symbol(): stock1,
        stock2.symbol(): stock2,
        stock3.symbol(): stock3,
        stock4.symbol(): stock4,
        stock5.symbol(): stock5
        }
    print("Symbol | Company Name")

    for symbol, stock in stocks.items():
        print(f"{symbol} : {stock.company_name()}")



