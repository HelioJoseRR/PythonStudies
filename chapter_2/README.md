# Variables and Simple Data Types

This is the appendix for this chapter:

- [Introduction](#Introduction)
- [Variable](#variables)
    - [Strings](#strings)
    - [Numbers](#numbers)
- [The Zen Of Python](#the-zen-of-python)

You can also find the codes from this section in the [codes](./codes) directory.

## Introduction

This chapter introduces Python data variables and how you can work with them.

## Variables

This simple code explains how a variable works:

```python
message = "Hello Python World!"
print(message)
```

Run this program to see what happens. The output should be displayed on your screen:

```
Hello Python World!
```

We've created a variable named `message` and assigned the value "Hello Python World!" to it.

### Naming and Using Variables

Here are some rules for naming a variable:

| Rules |
|---|
| Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number. |
| Spaces are not allowed in variable names; instead, use underscores to separate words. |
| Avoid using Python keywords and function names as variable names. |
| Variable names should be concise yet descriptive. |
| Be cautious when using the lowercase letter `l` and the uppercase letter `O`, as they may be confused with the numbers `1` and `0`. |

### Variables and Labels

As the book says:

> It’s much better to think of variables as labels that you can assign to values. You can also say that a variable references a certain value.

> [Try It Yourself 2.1 and 2.2](./codes)

### Strings

You can use single or double quotes around strings:

```python
"This is a string"
'This is also a string'
```

To use quotes and apostrophes within strings, alternate between single and double quotes:

```python
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
```

#### Methods

```python
name = "ada lovelace"
print(name.title())
```

Output:

```python
Ada Lovelace
```

> A method is an action that Python can perform on a piece of data.

Other methods mentioned in this chapter include:

```python
name.upper()  # Prints the string in uppercase
name.lower()  # Prints the string in lowercase
```

#### Using Variables in Strings

You can combine two values to display someone's full name:

```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
```

The `f` stands for `format`, and these strings are known as f-strings.

The code output is:

```python
ada lovelace
```

Using methods with f-strings:

```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
```

#### Adding Whitespace to Strings with Tabs or Newlines

To include tabs and newlines in your strings, add `\t` for tabs and `\n` for newlines.

#### Stripping Whitespace

You can remove leading or trailing whitespace from strings using the following methods: `.rstrip()` removes trailing whitespace, `.lstrip()` removes leading whitespace, and `.strip()` removes both leading and trailing whitespace.

```python
>>>name = " python "
>>>print(name.lstrip())
"python "

>>>print(name.rstrip())
" python"

>>>print(name.strip())
"python"
```

#### Removing Prefixes

It is easily done by using the `.removeprefix('prefix')` method.

```python
site = "https://google.com"
print(site.removeprefix('https://'))

# Output: google.com
```

> [Try It Yourself 2.3 - 2.8](./codes/)

### Numbers

Here are some operations in Python:

| Symbol | Meaning |
| --- | --- |
| `+` | Add |
| `-` | Subtract |
| `*` | Multiply |
| `/` | Divide |
| `**` | Exponents |

#### Integers and Floats

> When you divide any two numbers, even if they are integers that result in a whole number, you’ll always get a float.

> If you mix an integer and a float in any other operation, you’ll get a float as well.

You can group digits of large numbers with an underscore for readability: `1_000_000` is equivalent to `1000000`.

#### Constants

> Python doesn’t have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed.

> [Try It Yourself 2.9 and 2.10](./codes/)

## The Zen of Python

> Beautiful is better than ugly.  
> Explicit is better than implicit.  
> Simple is better than complex.  
> Complex is better than complicated.  
> Flat is better than nested.  
> Sparse is better than dense.  
> Readability counts.  
> Special cases aren't special enough to break the rules.  
> Although practicality beats purity.  
> Errors should never pass silently.  
> Unless explicitly silenced.  
> In the face of ambiguity, refuse the temptation to guess.  
> There should be one—and preferably only one—obvious way to do it.  
> Although that way may not be obvious at first unless you're Dutch.  
> Now is better than never.  
> Although never is often better than *right* now.  
> If the implementation is hard to explain, it's a bad idea.  
> If the implementation is easy to explain, it may be a good idea.  
> Namespaces are one honking great idea—let's do more of those!