class Product:
    def __init__(self, name: str, price: float, in_stock: int):
        self.name = name
        self.price = price
        self.__in_stock = in_stock
        
    @property
    def in_stock(self):
        return self.__in_stock
    
    def sell_product(self, quantity: int):
        if self.__in_stock >= quantity:
            self.__in_stock -= quantity
        else:
            print("Não há estoque para realizar a operação.")
    
    def buy_product(self, quantity: int):
        self.__in_stock += quantity
    
    def get_total_value(self):
        return self.__in_stock * self.price
