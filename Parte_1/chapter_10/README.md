# Files and Exceptions  

This is the appendix for this chapter:

1. [Introduction](#introduction)
2. [Reading from a File](#reading-from-a-file)
3. [Writing to a File](#writing-to-a-file)
4. [Exceptions](#exceptions)
5. [Analyzing Text](#analyzing-text)
6. [Storing Data](#storing-data)  

You can also find the codes from this section in the [codes](./codes) directory.  

[RETURN](./../../README.md)  

## Introduction  

In this chapter, you'll learn to work with files so your programs can quickly analyze lots of data.  

## Reading from a File  

```python
from pathlib import Path

path = Path('file_name.txt')
contents = path.read_text()
print(contents)
```  

Since the `file_name.txt` is in the same directory as the `.py` file, the filename is all the Path needs to access the file.  

### Relative and Absolute File Paths  

To get Python to open files from a directory other than the one where your program file is stored, you need to provide the correct path.  

A relative file path tells Python to look for a given location relative to the directory where the currently running program file is stored.  

```python
path = Path('text_files/filename.txt')
```  

You can also tell Python exactly where the file is on your computer, regardless of where the program that’s being executed is stored. This is called an absolute file path.  

```python
path = Path('/home/eric/data_files/text_files/filename.txt')
```  
### Accessing a File’s Lines  

You can use the splitlines() method to turn a long string into a set of lines, and then use a for loop to examine each line from a file, one at a time.  

```python
from pathlib import Path


path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)
```  

> When Python reads from a text file, it interprets all text in the file as a string. If you read in a number and want to work with that value in a numerical context, you’ll have to convert it to an integer using the int() function or a float using the float() function.  

>[TRY IT YOURSELF 10.1 - 10.3](./codes/)  

## Writing to a File  

### Writing a Single Line  

You can write a file using the `write_text()` method.  

```python
from pathlib import Path


path = Path('programming.txt')
path.write_text("I love programming.")
```  

>Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.  

### Writing Multiple Lines  

To write more than one line to a file, you need to build a string containing the entire contents of the file, and then call write_text() with that string.  

```python
from pathlib import Path


contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path = Path('programming.txt')
path.write_text(contents)
```  

>Be careful when calling write_text() on a path object. If the file already exists, write_text() will erase the current contents of the file and write new contents to the file. Later in this chapter, you’ll learn to check whether a file exists using pathlib.  

>[TRY IT YOURSELF 10.4 - 10.5](./codes/)  

## Exceptions  

Python uses special objects called exceptions to manage errors that arise during a program’s execution. Whenever an error occurs that makes Python unsure of what to do next, it creates an exception object. If you write code that handles the exception, the program will continue running. If you don’t handle the exception, the program will halt and show a traceback, which includes a report of the exception that was raised.  

Exceptions are handled with try-except blocks.  

### Handling the ZeroDivisionError Exception  

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```  

### The else Block  

```python
--snip--
while True:
    --snip--
    if second_number == 'q':
        break
    try:
        answer = int(first_num) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```  

### Handling the FileNotFoundError Exception  

Let’s try to read a file that doesn’t exist.  

```python
from pathlib import Path


path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
```  

## Analyzing Text  

Let’s pull in the text of Alice in Wonderland and try to count the number of words in the text.  

```python
from pathlib import Path


path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
```  

### Failing Silently  

Sometimes, you’ll want the program to fail silently when an exception occurs and continue on as if nothing happened. To make a program fail silently, you write a try block as usual, but you explicitly tell Python to do nothing in the except block. Python has a pass statement that tells it to do nothing in a block:  

```python
try:
    --snip--
except ErrorName:
    pass
else:
    --snip--
```  

>[TRY IT YOURSELF 10.6 - 10.10](./codes/)  

## Storing Data  

When users close
a program, you’ll almost always want to save the information they entered. A simple way to do this involves storing your data using the json module.  

### Using `json.dumps()` and `json.loads()`  

The json.dumps() function takes one argument: a piece of data that should be converted to the JSON format.  

```python
from pathlib import Path
import json


numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)
```  

Now we’ll write a separate program that uses json.loads() to read the list back into memory:  

```python
from pathlib import Path
import json


path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
```  

>[TRY IT YOURSELF 10.11 - 10.12](./codes/)  
