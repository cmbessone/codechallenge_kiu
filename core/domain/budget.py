from datetime import date

class Budget:
    def __init__(self, id: int, provider: str, article: str,
                  quantity_planned:int, price_per_unit:int,planned_date:date):
        self.id = id
        self.provider = provider
        self.article = article
        self.quantity_planned = quantity_planned
        self.price_per_unit = price_per_unit
        
        if quantity_planned < 0 or price_per_unit < 0:
            raise ValueError('Quantity planned must be greater than 0')
        
        self.total_amount = quantity_planned * price_per_unit
        self.planned_date = planned_date


    def __str__(self):
        return {f"Budget(id={self.id},
        provider={self.provider},
        article: {self.article},
        quantity_planned: {self.quantity_planned},
        price_per_unit: {self.price_per_unit},
        total_amount: {self.total_amount},
        planned_date: {self.planned_date}"}