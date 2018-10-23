class Phone:
    def __init__(self,price,brand):
        self.price = price
        self.brand = brand
        print("Test the init")
    def getprice(self):
            print("Price: %s" %self.price)
    def getbrand(self):
            print("Mobile brand: %s" %self.brand)
