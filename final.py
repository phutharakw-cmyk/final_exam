class Person:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}")
        
class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address
    
    def place_order(self,item):
        self.this_order =  DeliveryOrder(self,item,"preparing")
    
class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle

    def deliver(self,order):
        print(f"{self.name} is delivering {order[1]} to {order[0]} using {self.vehicle}.")

class DeliveryOrder:
    def __init__(self, customer, item , status):
        self.customer = customer
        self.item = item
        self.staus = status

    def assign_driver(self,driver):
        self.driver = driver

    def delivery_item(self):
        self.driver.deliver([self.customer.name,self.item])
        self.staus = "delivered"
        print(f"Order for {self.item} → {self.staus}")

    def summary(self):
        print("Order Summary:")
        print(f"tem: {self.item}")
        print(f"Customer: {self.customer.name}")
        print(f"Status: {self.staus}")
        print(f"Driver: {self.driver.name}")
        
#creat a customer and driver
customer_1 = Customer("Alice","Home")
customer_2 = Customer("Bob","Home")
driver_1 = Driver("David","Middle of nowhere")

#let the customer and driver introduce their name
customer_1.introduce()
customer_2.introduce()
driver_1.introduce()
print()

#creat the oder for any customer
customer_1.place_order("labtop")
customer_2.place_order("Headphones")

#assign the driver to the customer 1
customer_1.this_order.assign_driver(driver_1)
customer_1.this_order.summary()
print()

#assign the driver to the customer 2
customer_2.this_order.assign_driver(driver_1)
customer_2.this_order.summary()
print()

#let the deriver delivery the item to customer
customer_1.this_order.delivery_item()
customer_2.this_order.delivery_item()
print()

#update final status
print("Final Status:")
print(f"Order for {customer_1.this_order.item} → {customer_1.this_order.staus}")
print(f"Order for {customer_2.this_order.item} → {customer_2.this_order.staus}")
