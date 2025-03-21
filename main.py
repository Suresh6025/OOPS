class Item:

    pay_rate=0.8 # price discount after 20% discount
    # Constructor - self function for class , which passes the parameters 
    def __init__(self,name:str,price:float,quantity:int):

        # Add validation to recieve the arguments
        assert price>=0,f"Price {price} must be equal to or greater than zero"
        assert quantity>=0,f"Quantity {quantity} must be equal to or greater than zero"

        #Assign to self object
        self.name=name
        self.price=price  # instance attributes- which is used inside constructor
        self.quantity=quantity

    # Functions inside class are called methods
    def calculate_total_price(self):
        return self.price*self.quantity
    
    #Apply discount on the price
    def apply_discount(self):
        self.price=self.price * Item.pay_rate

item1 = Item("phone",1000,3)

item1.apply_discount()
print(item1.price)

#print(Item.__dict__) #Magic methods- which gives us all the attributes present inside the classes
