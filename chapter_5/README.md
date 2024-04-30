# If Statements

This is the appendix for this chapter:

1. [Introduction](#introduction)
2. [A Simple Example](#a-simple-example)
3. [Conditional Tests](#conditional-tests)
    - [Checking for Equality](#checking-for-equality)
    - [Ignoring Case When Checking for Equality](#ignoring-case-when-checking-for-equality)
    - [Checking for Inequality](#checking-for-inequality)
    - [Numerical Comparisons](#numerical-comparisons)
    - [Checking Multiple Conditions](#checking-multiple-conditions)
    - [Using `and` to Check Multiple Conditions](#using-and-to-check-multiple-conditions)
    - [Using `or` to Check Multiple Conditions](#using-or-to-check-multiple-conditions)
    - [Checking Whether a Value Is in a List](#checking-whether-a-value-is-in-a-list)
    - [Checking Whether a Value Is Not in a List](#checking-whether-a-value-is-not-in-a-list)
    - [Boolean Expressions](#boolean-expressions)
4. [If Statements](#if-statements)
    - [Simple if Statements](#simple-if-statements)
    - [if-else Statements](#if-else-statements)
    - [The if-elif-else Chain](#the-if-elif-else-chain)
    - [Using if Statements with Lists](#using-if-statements-with-lists)
    - [Checking That a List Is Not Empty](#checking-that-a-list-is-not-empty)
    - [Using Multiple Lists](#using-multiple-lists)

You can also find the codes from this section in the [codes](./codes) directory.

## Introduction  

In this chapter, you’ll learn to write conditional tests, which allow you to check any condition of interest.

## A Simple Example  

Let's use this car example:

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Output: Audi BMW Subaru Toyota
```

## Conditional Tests  

An expression that can be evaluated as True or False.

### Checking for Equality  

```python
car = 'bmw'
car == 'bmw'  # True
``` 

### Ignoring Case When Checking for Equality  

Testing for equality is case-sensitive in Python.

```python
car = 'Audi'
car == 'audi'  # False
```

```python
car = 'Audi'
car.lower() == 'audi'  # True    
```

### Checking for Inequality  

When you want to determine whether two values are not equal, you can use the inequality operator (`!=`).

```python
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Output: Hold the anchovies!
```  

### Numerical Comparisons  

```python
age = 18
age == 18  # True
```  

```python
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

# Output: That is not the correct answer. Please try again!
```  

You can include various mathematical comparisons in your conditional statements as well, such as less than (`<`), less than or equal to (`<=`), greater than (`>`), and greater than or equal to (`>=`).

## Checking Multiple Conditions  

### Using `and` to Check Multiple Conditions  

You use `and` to check if two conditions are both true simultaneously.

```python
age_0 = 22
age_1 = 18
(age_0 >= 21) and (age_1 >= 21)  # False

age_1 = 22
(age_0 >= 21) and (age_1 >= 21)  # True
```

### Using `or` to Check Multiple Conditions  

You use `or` to check if at least one of the conditions is true.

```python
age_0 = 22
age_1 = 18
(age_0 >= 21) or (age_1 >= 21)  # True

age_0 = 18
(age_0 >= 21) or (age_1 >= 21)  # False
```

## Checking Whether a Value Is in a List  

To find out whether a particular value is already in a list, use the keyword `in`.

```python
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings  # True
'pepperoni' in requested_toppings  # False
```  

### Checking Whether a Value Is Not in a List  

To find out whether a particular value isn't in a list, use the keyword `not`.

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")  

# Output: Marie, you can post a response if you wish.
```  

## Boolean Expressions  

A Boolean expression is just another name for a conditional test.

```python
game_active = True
can_edit = False
```  

> [Try It Yourself 5.1](./codes/)  

## If Statements  

### Simple if Statements  

```python
if conditional_test:
    do something
```  

### if-else Statements  

An if- else block is similar to a simple if statement, but the else statement allows you to define an action or set of actions that are executed when the conditional test fails.

```python
if conditional_test:
    do something
else:
    do something
```  

### The if-elif-else Chain  

Often, you’ll need to test more than two possible situations, and to evaluate these, you can use Python’s if-elif-else syntax.

```python
if conditional_test:
    do something
elif conditional_test_2:
    do something
elif conditional_test_3:
    do something
else:
    do something
```  

Python does not require an else block at the end of an if-elif chain.

> [Try It Yourself 5.3 - 5.6](./codes/)  

## Using if Statements with Lists  

### Checking That a List Is Not Empty  

Instead of jumping right into a for loop, we do a quick check first.

```python
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
    else:
        print("Are you sure you want a plain pizza?")
```  

### Using Multiple Lists  

```python
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
```

> [Try It Yourself 5.8 - 5.11](./codes/)  