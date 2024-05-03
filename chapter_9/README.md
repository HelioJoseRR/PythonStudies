## Classes

This is the appendix for this chapter:

1. [Introduction](#introduction)

You can also find the codes from this section in the [codes](./codes) directory.  


## Introduction  

In this chapter, you will learn about Object-Oriented Programming (OOP).  

Making an object from a class is called instantiation. In this chapter, you’ll write classes and create instances of those classes.  

## Creating and Using a Class  

### Creating the Dog Class  

Each instance created from the Dog class will store a name and an age, and we’ll give each dog the ability to sit() and roll_over():  

```python
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!.")
```  

We first defined a class called Dog. By convention, capitalized names refer to classes in Python.  

### The `__init__()` Method  

A function that's part of a class is a method. The `__init__()` method is a special method that Python runs automatically whenever we create a new instance based on the Dog class.  

The self parameter is required in the method definition, and it must come first.  

### Making an Instance from a Class  

```python
class Dog:
    --snip--

my_dog = Dog('willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's {my_dog.age} years old.")
```  

#### Accessing Attributes  

To access the attributes of an instance, you use dot notation. 

```python
my_dog.name
```  

Here, Python looks at the instance `my_dog` and then finds the attribute `name` associated with `my_dog`.  

#### Calling Methods  

After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog.  

```python
class Dog:
    --snip--

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()
```  

#### Creating Multiple Instances  

```python
class Dog:
    --snip--

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```  
>[TRY IT YOURSELF 9.1 - 9.3](./codes/)  

## Working with Classes and Instances  

One of the first tasks you’ll want to do is modify the attributes associated with a particular instance. You can modify the attributes of an instance directly or write methods that update attributes in specific ways.  

### The Car Class  

```python
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# output: 2024 Audi A4
```  

### Setting a Default Value for an Attribute  

When an instance is created, attributes can be defined without being passed in as parameters. These attributes can be defined in the `__init__()` method, where they are assigned a default value.  

```python
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# output: 2024 Audi A4 
# This car has 0 miles on it.
```   

### Modifying Attribute Values  

#### Modifying an Attribute's Value Directly  

```python
class Car:
    --snip--

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# output: 2024 Audi A4 
# This car has 23 miles on it.
```  

#### Modifying an Attribute’s Value Through a Method  

```python
class Car:
    --snip--
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

# output: 2024 Audi A4 
# This car has 23 miles on it.
```  

#### Incrementing an Attribute’s Value Through a Method  

```python
    class Car:
        --snip--
    
    def update_odometer(self, mileage):
        --snip--

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# output:
# 2019 Subaru Outback
# This car has 23500 miles on it. 
# This car has 23600 miles on it.
```  

>[TRY IT YOURSELF 9.4 - 9.5](./codes/)  

## Inheritance  

You don’t always have to start from scratch when writing a class. If the class you’re writing is a specialized version of another class you wrote, you can use inheritance. The original class is called the parent class, and the new class is the child class.  

### The `__init__()` Method for a Child Class  

When you’re writing a new class based on an existing class, you’ll often want to call the `__init__()` method from the parent class. This will initialize any attributes that were defined in the parent `__init__()` method and make them available in the child class.  

```python
class Car:
    --snip--

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name()) 
```  

We start with Car. When you create a child class, the parent class must be part of the current file and must appear before the child class in the file. We then define the child class, ElectricCar. The name of the parent class must be included in parentheses in the definition of a child class. The `__init__()` method takes in the information required to make a Car instance.  

The super() function is a special function that allows you to call a method from the parent class. This line tells Python to call the `__init__()` method from Car, which gives an ElectricCar instance all the attributes defined in that method. The name super comes from a convention of calling the parent class a superclass and the child class a subclass.  

### Defining Attributes and Methods for the Child Class  

```python
class Car:
    --snip--

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf = ElectricCar('nissan', 'leaf', 2024)

print(my_leaf.get_descriptive_name())

my_leaf.describe_battery()

# OUTPUT: 
# 2024 Nissan Leaf
# This car has a 40-kWh battery.
```  

### Overriding Methods from the Parent Class  

To do this, you define a method in the child class with the same name as the method you want to override in the parent class.  

### Instances as Attributes  

You can break your large class into smaller classes that work together; this approach is called *composition*.  

```python
class Car:
    --snip--

class Battery:

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    --snip--
    self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
```  

>[TRY IT YOURSELF 9.6 - 9.8](./codes/)  






