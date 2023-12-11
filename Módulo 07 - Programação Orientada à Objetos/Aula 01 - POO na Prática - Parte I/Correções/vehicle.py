from datetime import datetime

class Vehicle:
    __depreciation_rate = 0.05
    __percentage_tax = 0.02
    
    def __init__(self, brand: str, year: int, base_value: float):
        self.brand = brand
        self.year = year
        self.base_value = base_value
        
    def calculate_tax(self):
        vehicle_age = datetime.now().year - self.year
        deprecated_value = self.base_value * (1 - Vehicle.__depreciation_rate) ** vehicle_age
        return deprecated_value * Vehicle.__percentage_tax
        
        
        