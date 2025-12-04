# Delivery order simulation 

This is a oop Python code that show the method and simulation the delivery order
that have customer driver and each have their function in it.

---

## File Structure

- `final.py`: The main Python program that contains all the classes and method

---

## Classes Overview
- Person : that is a parent class.
- Customer : the person that buy an item and the driver need to deliver item to them.
- Driver : the person that devery item to customers.
- Delivery order : the class that came after the customer order and have the delivery method.

### Methods
#### For Person
- `lintroduce` : they can say hi and there name.
#### For Customer  
- `place_order` : they can place order to driver.
#### For Driver
- `deliver` : this is show thing that driver have to do
#### For Delivery order.
- `assign_driver` : to put a driver to the customer
- `delivery_item` : to get the driver delivery the item and update status.
- `summary` : to print all of data that have like customer name item or driver name.

## How the Code Works and run

the code can creat the customer and driver and it will simulate the delivery oder and show it in the output

---

## Running the Program

To run the program, open a terminal in this folder and execute:

```bash
python final.py

