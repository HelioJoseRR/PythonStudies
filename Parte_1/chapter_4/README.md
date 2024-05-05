# Working with Lists  

This is the appendix for this chapter:

- [Introduction](#introduction)
- [Looping Through an Entire List](#looping-through-an-entire-list)
- [Avoiding Indentation Errors](#avoiding-indentation-errors)
- [Making Numerical Lists](#making-numerical-lists)
    - [Using the `range()` Function](#using-the-range-function)
    - [Using `range()` to Make a List of Numbers](#using-range-to-make-a-list-of-numbers)
    - [Simple Statistics with a List of Numbers](#simple-statistics-with-a-list-of-numbers)
    - [List Comprehensions](#list-comprehensions)
- [Working with Part of a List](#working-with-part-of-a-list)
    - [Slicing a List](#slicing-a-list)
    - [Copying a List](#copying-a-list)
- [Tuples](#tuples)
    - [Defining a Tuple](#defining-a-tuple)
- [Styling Your Code](#styling-your-code)

You can also find the codes from this section in the [codes](./codes) directory.  

[RETURN](./../../README.md)  

## Introduction  

In this chapter, you will learn how to loop through an entire list.

## Looping Through an Entire List  

Using a for loop:

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```

> You can also write as many lines of code as you like in the for loop. Every indented line following the line `for magician in magicians` is considered inside the loop, and each indented line is executed once for each value in the list.

## Avoiding Indentation Errors  

> Python uses indentation to determine how a line, or group of lines, is related to the rest of the program. In the previous examples, the lines that printed messages to individual magicians were part of the for loop because they were indented.

> [Try It Yourself 4.1](./codes/)

## Making Numerical Lists  

### Using the `range()` Function  

> You can use the `range()` function to print a series of numbers like this:  

```python
for value in range(1, 5):
    print(value)
# Output: 1 2 3 4
```

> You can also pass `range()` only one argument, and it will start the sequence of numbers at 0. For example, `range(6)` would return the numbers from 0 through 5.

### Using `range()` to Make a List of Numbers  

```python
numbers = list(range(1, 6))
print(numbers)
# Output: [1, 2, 3, 4, 5]
```

You can use the `range()` function to tell Python to skip numbers in a given range. If you pass a third argument, here's how to print even numbers:

```python
even_numbers = list(range(2, 11, 2))
print(even_numbers)
# Output: [2, 4, 6, 8, 10]
```

### Simple Statistics with a List of Numbers  

A few helpful Python functions:

```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))  # Output: 0
print(max(digits))  # Output: 9
print(sum(digits))  # Output: 45
```

### List Comprehensions  

> A list comprehension allows you to generate this same list in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line and automatically appends each new element.

```python
squares = [value**2 for value in range(1, 11)]
print(squares)

# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

> [Try It Yourself 4.3 - 4.9](./codes/)

## Working with Part of a List  

### Slicing a List  

Specify the index of the first and last elements you want to work with:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# Output: ['charles', 'martina', 'michael']
```

> If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list.

> You can include a third value in the brackets indicating a slice. If a third value is included, this tells Python how many items to skip between items in the specified range.

### Copying a List  

> To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]).

> [Try It Yourself 4.10 - 4.11](./codes/)

## Tuples  

> However, sometimes you’ll want to create a list of items that cannot change. Tuples allow you to do just that. Python refers to values that cannot change as immutable, and an immutable list is called a tuple.

### Defining a Tuple  

You use parentheses instead of square brackets.

```python
dimensions = (200, 50)
print(dimensions[0])  # Output: 200
print(dimensions[1])  # Output: 50
```

> Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable. If you want to define a tuple with one element, you need to include a trailing comma.

## Styling Your Code  

> Python programmers have agreed on a number of styling conventions to ensure that everyone’s code is structured in roughly the same way. Once you’ve learned to write clean Python code, you should be able to understand the overall structure of anyone else’s Python code, as long as they follow the same guidelines.

> When someone wants to make a change to the Python language, they write a Python Enhancement Proposal (PEP). One of the oldest PEPs is PEP 8, which instructs Python programmers on how to style their code.

| Rule | Description |
| --- | --- |
| Indentation | PEP 8 recommends that you use four spaces per indentation level. |
| Line Length | Many Python programmers recommend that each line should be less than 80 characters. PEP 8 also recommends that you limit all of your comments to 72 characters per line. |
| Blank Lines | To group parts of your program visually, use blank lines. You should use blank lines to organize your files, but don’t do so excessively. |

> PEP 8 has many additional styling recommendations, but most of the guidelines refer to more complex programs than what you’re writing at this point. As you learn more complex Python structures, I’ll share the relevant parts of the PEP 8 guidelines.