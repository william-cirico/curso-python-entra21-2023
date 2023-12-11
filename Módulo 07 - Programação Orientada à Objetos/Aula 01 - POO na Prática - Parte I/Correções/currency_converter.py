class CurrencyConverter:
    tax_conversion = 4.93
    currency = "USD"
    

    @classmethod
    def convert_to_BRL(cls, value: float):
        return cls.tax_conversion * value
    

    @classmethod
    def convert_from_BRL(cls, value: float):
        return value / cls.tax_conversion