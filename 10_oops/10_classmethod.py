# class method and static method class method will take cls as an arguments 


class ChaiOrder:

    def __init__(self,item,size,company):
        self.item = item
        self.size = size
        self.company = company
    @classmethod
    def from_dict(cls,order_data):
        return cls(order_data['item'], order_data['size'], order_data['company'])
    
    @classmethod
    def from_string(cls,order_data):
        item, size, company = (order_data).split(",")
        return cls(item,size,company)
    
    @staticmethod
    def is_valid_size(size):
        return size in ['small','medium','large']
    
order1 = ChaiOrder.from_dict({"item":"tea","size" : "large", "company": "bru"})

print(order1.__dict__)

order2 = ChaiOrder.from_string("coffe,small,nescafe")

print(order2.__dict__)

order3 = ChaiOrder("coke","large","cola")

print(order3.__dict__)

print(ChaiOrder.is_valid_size("small"))
        