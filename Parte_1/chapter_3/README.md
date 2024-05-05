# Introducing Lists

This is the appendix for this chapter:

- [Introduction](#introduction)
- [What is a List?](#what-is-a-list)
- [Accessing Elements in a List](#accessing-elements-in-a-list)
- [Modifying, Adding, and Removing Elements](#modifying-adding-and-removing-elements)
- [Organizing a List](#organizing-a-list)
- [Finding the Length of a List](#finding-the-length-of-a-list)

You can also find the codes from this section in the [codes](./codes) directory.  

[RETURN](./../../README.md)  

## Introduction

> In this chapter and the next, you’ll learn what lists are and how to start working with the elements in a list.

## What Is a List?

Lists are collections of items in a particular order. In Python, square brackets `[]` indicate a list. It's best to name your list in the plural form.

### Example:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```

Output:

```python
['trek', 'cannondale', 'redline', 'specialized']
```

## Accessing Elements in a List

To access an element in a list, use its index:

```python
print(bicycles[0])  # Outputs: trek
```

The index position starts from 0, not 1. Additionally, you can use methods on lists.

Python has a special syntax for accessing the last element in a list. If you ask for the item at index -1, it will return the last item in the list.

> [Try It Yourself 3.1 - 3.2](./codes/)

## Modifying, Adding, and Removing Elements

Lists are dynamic.

### Modifying Elements in a List

To modify an element in a list, use the name of the list followed by the index of the element you want to change, and then provide the new value.

### Adding Elements to a List

Python provides several ways to add new data to existing lists.

#### Appending Elements to the End of a List

Use the method `.append('item')`.

#### Inserting Elements into a List

Use the method `.insert(index, 'item')` to insert an item at a specific position in the list. This operation shifts every other value in the list one position to the right.

### Removing Elements from a List

#### Using the `del` Statement

If you know the index of the item you want to remove, you can use the `del` statement:

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
```

#### Removing an Item Using the `pop()` Method

The `.pop()` method removes the last item from a list, but it lets you work with that item after removing it.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
```

You can use `pop()` to remove an item from any position in a list by including the index of the item you want to remove in parentheses.

#### Removing an Item by Value

If you know the value but not the index, you can use the `.remove('item')` method.

> The `remove()` method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to make sure all occurrences of the value are removed.

> [Try It Yourself 3.4 - 3.7](./codes/)

## Organizing a List

Python provides a number of different ways to organize your lists, depending on the situation.

### Sorting a List Permanently with the `sort()` Method

The `sort()` method changes the order of the list permanently. You can also sort this list in reverse-alphabetical order by passing the argument `reverse=True` to the `sort()` method.

#### Example:
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)  # Output: ['audi', 'bmw', 'subaru', 'toyota']

cars.sort(reverse=True)
print(cars)  # Output: ['toyota', 'subaru', 'bmw', 'audi']
```

### Sorting a List Temporarily with the `sorted()` Function

To maintain the original order of a list but present it in a sorted order, you can use the `sorted()` function.

#### Example:
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))  # Output: ['audi', 'bmw', 'subaru', 'toyota']
print(cars)  # Output: ['bmw', 'audi', 'toyota', 'subaru']
```

### Printing a List in Reverse Order

To reverse the original order of a list, you can use the `reverse()` method. `reverse()` doesn’t sort backward alphabetically; it simply reverses the order of the list.

#### Example:
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)  # Output: ['subaru', 'toyota', 'audi', 'bmw']
```

## Finding the Length of a List

You can quickly find the length of a list by using the `len()` function.

#### Example:
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))  # Output: 4
```

> [Try It Yourself 3.8 - 3.9](./codes/)