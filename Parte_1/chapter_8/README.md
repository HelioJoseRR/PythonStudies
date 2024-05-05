## Functions

This is the appendix for this chapter:

1. [Introduction](#introduction)

You can also find the codes from this section in the [codes](./codes) directory.  

[RETURN](./../../README.md)  

## Introduction  

In this chapter you’ll learn how to write functions.  

## Defining a Function  

```python
def greet_user():
    print("Hello!")

greet_user()

# output: Hello!
```  

The first line uses the keyword `def` to inform Python that you're defining a function. After we have the name of the function and the parameters, which we have none in this example. Any indented lines that follows make up the body of the function.  

### Passing Information to a Function  

```python
def greet_user(username):
    print(f"Hello, {username.title()}!")

greet_user('Jesse')

# output: Hello, Jesse!
```  

### Arguments and Parameters  

```python
def greet_user(username):
    print(f"Hello, {username.title()}!")

greet_user('Jesse')

# output: Hello, Jesse!
```  

Using the same example, `username` is a parameter and `Jesse` is an argument.  

> [TRY IT YOURSELF 8.1 - 8.2](./codes/)

## Passing Arguments  

### Positional Arguments  

When you call a function, Python must match each argument in the function call with a parameter in the function definition.  

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# output: I have a hamster.
# My hamster's name is Harry
```  

You can call a function as many times as needed. Also, the order of the arguments matters.  

## Keyword Arguments  

A keyword argument is a name-value pair that you pass to a function. 

The order of the arguments doesn't matter.  

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

# output: I have a hamster.
# My hamster's name is Harry
```  
> When you use keyword arguments, be sure to use the exact names of the parameters in the function’s definition.  

## Default Values  

When writing a function, you can define a default value for each parameter.  

```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# output: I have a dog.
# My hamster's name is Willie.
```  

> When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly.  

> [TRY IT YOURSELF 8.3 - 8.4](./codes/)  

## Return Values

A function can return a value; it's called a "return value."

### Returning a Simple Value

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}" 
    return full_name.title()

musician = get_formatted_name('Jimi', 'Hendrix')
print(musician)

# output: Jimi Hendrix
```

If you want to make an argument optional, you could set the value of an empty string to it and check the value.

```python
def optional(first, second, third=""):
    if third:
        print(f"{first} {second} {third}")
    else:
        print(f"{first} {second}")
```

### Returning a Dictionary

```python
def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}

    if age:
        person['age'] = age

    return person

musician = build_person('Jimi', 'Hendrix', age=27)
print(musician)

# output: {'first': 'Jimi', 'last': 'Hendrix', 'age': 27}
```

>[TRY IT YOURSELF 8.6 - 8.8](./codes/)  

## Passing a List  

```python
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# output: 
# Hello, Hannah!
# Hello, Ty! 
# Hello, Margot!
```  

### Modifying a List in a Function  

Any changes made in the function are permanent when you pass a list to it.  

If you don't want the function to modify your list, you can send the list like this:  

```python
function_name(list_name[:])
```

By adding `[:]` to the list name, you send a copy of the list to the function.  

>[TRY IT YOURSELF 8.9 - 8.11](./codes/)  

## Passing an Arbitrary Number of Arguments  

If you don't know how many arguments the function accepts, you can define your parameters like this:  

```python
def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# output:  
# ('pepperoni',)
# ('mushrooms', 'green peppers', 'extra cheese')
```  

As you can see, Python packs the arguments into a tuple.  

### Mixing Positional and Arbitrary Arguments  

Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.  

> You’ll often see the generic parameter name *args, which collects arbitrary positional arguments like this.  

### Using Arbitrary Keyword Arguments  

You can write functions that accept as many key-value pairs as the calling statement provides.  

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                              location='princeton',
                              field='physics')
print(user_profile)

""" output: 
{'location': 'princeton', 'field': 'physics',
'first_name': 'albert', 'last_name': 'einstein'}
"""
```  

The double asterisks before the parameter user_info cause Python to create a dictionary called `user_info`.  

> You’ll often see the parameter name **kwargs used to collect nonspecific keyword arguments.  

>[TRY IT YOURSELF 8.12 - 8.14](./codes/)  

## Storing Your Functions in Modules  

You can store your functions in a separate file called a `module` and then import that module into your main program.  

### Importing an Entire Module  

A module is a file ending in `.py` that contains the code you want to import into your program.  

If you make a module called `pizza.py`, you have to import it like this in your code:  

```python  
import pizza

pizza.make_pizza()
```  

As you can see, to call a function in the `pizza` module, you have to write its name, followed by a dot and the function name.  

### Importing Specific Functions  

You can also import a specific function from a module. Here’s the general syntax for this approach:  

```python  
from pizza import make_pizza, pizza_toppings, price_pizza
```  

### Using `as` to Give a Function an Alias  

If the name of a function you’re importing might conflict with an existing name in your program, or if the function name is long, you can use a short, unique alias—an alternate name similar to a nickname for the function.  

```python
from pizza import make_pizza as mp

mp()
```  

### Using `as` to Give a Module an Alias  

```python
import pizza as p

p.function()
```  

### Importing All Functions in a Module  

```python
from pizza import *

function()
```  

Because every function is imported, you can call each function by name without using the dot notation.  

## Styling Functions  

Functions should have descriptive names, and these names should use lowercase letters and underscores.  

Every function should have a comment that explains concisely what the function does. This comment should appear immediately after the function definition and use the docstring format.  

If you specify a default value for a parameter, no spaces should be used on either side of the equal sign:  

```python
def function_name(parameter_0, parameter_1='default value')
```  

The same convention should be used for keyword arguments in function calls.  

If your program or module has more than one function, you can separate each by two blank lines to make it easier to see where one function ends and the next one begins.  

All import statements should be written at the beginning of a file.  



