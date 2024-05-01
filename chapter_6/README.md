# Dictionaries  

This is the appendix for this chapter:

1. [Introduction](#introduction)
2. [A Simple Dictionary](#a-simple-dictionary)
3. [Working with Dictionaries](#working-with-dictionaries)
    - [Accessing Values in a Dictionary](#accessing-values-in-a-dictionary)
    - [Adding New Key-Value Pairs](#adding-new-key-value-pairs)
    - [Starting with an Empty Dictionary](#starting-with-an-empty-dictionary)
    - [Modifying Values in a Dictionary](#modifying-values-in-a-dictionary)
    - [Removing Key-Value Pairs](#removing-key-value-pairs)
    - [Using get() to Access Values](#using-get-to-access-values)
4. [Looping Through a Dictionary](#looping-through-a-dictionary)
    - [Looping Through All Key-Value Pairs](#looping-through-all-key-value-pairs)
    - [Looping Through All the Keys in a Dictionary](#looping-through-all-the-keys-in-a-dictionary)
    - [Looping Through a Dictionary’s Keys in a Particular Order](#looping-through-a-dictionarys-keys-in-a-particular-order)
    - [Looping Through All Values in a Dictionary](#looping-through-all-values-in-a-dictionary)
5. [Nesting](#nesting)
    - [A List of Dictionaries](#a-list-of-dictionaries)
    - [A List in a Dictionary](#a-list-in-a-dictionary)
    - [A Dictionary in a Dictionary](#a-dictionary-in-a-dictionary)  

You can also find the codes from this section in the [codes](./codes) directory.  

## Introduction  

Python’s dictionaries allow you to connect pieces of related information.  

## A Simple Dictionary  

```python
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# Output:
# green
# 5
```  

## Working with Dictionaries  

A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key.  

### Accessing Values in a Dictionary  

To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets.  

```python
alien_0 = {'color': 'green'}
print(alien_0['color'])
```  

### Adding New Key-Value Pairs  

Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time.  

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Output:
# {'color': 'green', 'points': 5}
# {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```  

### Starting with an Empty Dictionary  

To start filling an empty dictionary, define a dictionary with an empty set of braces and then add each key-value pair on its own line.  

```python
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0) 

# Output: {'color': 'green', 'points': 5} 
```  

### Modifying Values in a Dictionary  

To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key.  

```python
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# Output:
# The alien is green.
# The alien is now yellow.
```  

### Removing Key-Value Pairs  

When you no longer need a piece of information that’s stored in a dictionary, you can use the del statement to completely remove a key-value pair.  

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# Output: 
# {'color': 'green', 'points': 5}
# {'color': 'green'}
```  

### Using get() to Access Values  

For dictionaries specifically, you can use the get() method to set a default value that will be returned if the requested key doesn’t exist.  

The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn’t exist:  

```python
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')

print(point_value)

# Output: No point value assigned.
```  

> [TRY IT YOURSELF 6.1 - 6.2](./codes/)  

## Looping Through a Dictionary  

You can loop through all of a dictionary’s key-value pairs, through its keys, or through its values.  

### Looping Through All Key-Value Pairs  

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```  

The `items()` method returns a sequence of key-value pairs.  

### Looping Through All the Keys in a Dictionary  

Use the `keys()` method  

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())
```  

Looping through the keys is actually the default behavior when looping through a dictionary.  

### Looping Through a Dictionary’s Keys in a Particular Order  

One way to do this is to sort the keys as they’re returned in the for loop. You can use the `sorted()` function to get a copy of the keys in order:  

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```  

### Looping Through All Values in a Dictionary  

Use the `values()` method to return a sequence of values without any keys.  

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())
```  

To see each language chosen without repetition, we can use a set. A set is a collection in which each item must be unique.  

```python
favorite_languages = {
    --snip--
}

print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):
    print(language.title())
```  

> [TRY IT YOURSELF 6.5](./codes/)  

## Nesting  

Sometimes you’ll want to store multiple dictionaries in a list, or a list of items as a value in a dictionary. This is called nesting.  

### A List of Dictionaries  

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```  

### A List in a Dictionary  

```python
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza " "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
```  

### A Dictionary in a Dictionary  

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```

> [TRY IT YOURSELF 6.7 - 6.10](./codes/)  