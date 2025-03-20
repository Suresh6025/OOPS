class Item:
    # Constructor - self function for class , which passes the parameters 
    def __init__(self,name:str,price:float,quantity:int):

        # Add validation to recieve the arguments
        assert price>=0,f"Price {price} must be equal to or greater than zero"
        assert quantity>=0,f"Quantity {quantity} must be equal to or greater than zero"

        #Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity

    # Functions inside class are called methods
    def calculate_total_price(self):
        return self.price*self.quantity

item1 = Item("phone",1000,3.0)
item2 = Item("Laptop",500,-2)

print(item1.calculate_total_price())
print(item2.calculate_total_price())