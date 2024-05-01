## User Input and While Loops

This is the appendix for this chapter:

1. [Introduction](#introduction)
2. [Introducing while Loops](#introducing-while-loops)
3. [Using a while Loop with Lists and Dictionaries](#using-a-while-loop-with-lists-and-dictionaries)

You can also find the codes from this section in the [codes](./codes) directory.  


## Introduction  

In this chapter you’ll learn how to accept user input so your program can then work with it.  


## How the input() Function Works  

The input() function pauses your program and waits for the user to enter some text.  


### Writing Clear Prompts  

Each time you use the input() function you should write a clear prompt to instruct the user what they should write.  

```python
name = input("Please enter your name: ")
```  

You should also write a space at the end to visually show the user that they should write the input.  

To write a longer prompt you could use a variable:  

```python
prompt = "If you share your name, we can personalize the messages you see."  
prompt += "\nWhat is your first name? " 

name = input(prompt) 
```  

### Using int() to Accept Numerical Input  

When using the input function, Python interprets the input as a string. The int() function converts the input string to a numerical value.  

```python
>>> age = input("How old are you? ")
How old are you? 21  
>>> age = int(age)
>>> age >= 18
True
```  

### The Modulo Operator  

The modulo operator % divides one number by another and returns the remainder.  

```python
>>> 4 % 3
1
```  

> [TRY IT YOURSELF 7.1 - 7.3](./codes/)  

## Introducing while Loops  

> The for loop takes a collection of items and executes a block of code once for each item in the collection. In contrast, the while loop runs as long as, or while, a certain condition is true.  

### The while Loop in Action  

```python
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1

# output: 
# 1 
# 2 
# 3 
# 4 
# 5
```  

### Letting the User Choose When to Quit  

We can define a quit value and then keep the program running as long as the user has not entered the quit value.  

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)
    print(message)
```  

### Using a Flag  

For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active.  

```python
active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
```  

### Using break to Exit a Loop  

To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement.  

```python
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        command line
```  

### Using continue in a Loop  

Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the loop, based on the result of a conditional test.  

```python
current_number = 0

while current_number < 10:
    current_number += 1
    
    if current_number % 2 == 0:
        continue
    print(current_number)

# output: 1 3 5 7 9
```  

> [TRY IT YOURSELF 7.4 - 7.5](./codes/)  

## Using a while Loop with Lists and Dictionaries  

```python
unconfirmed_users = ['a', 'b', 'c']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# output: A B C
```  

### Removing All Instances of Specific Values from a List  

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# output: 
# ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# ['dog', 'dog', 'goldfish', 'rabbit']
```  

### Filling a Dictionary with User Input  

```python
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")

    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")

for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
```  

> [TRY IT YOURSELF 7.8 - 7.10](./codes/)  