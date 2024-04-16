
# Getting Started

This is the appendix for this chapter:  
- [Introduction](#introduction)
- [Python on Different Operating Systems](#python-on-different-operating-systems)
    - [Windows](#windows)
    - [MacOS](#macos)
    - [Linux](#linux)
- [Running a Hello World Program](#running-a-hello-world-program)
- [Troubleshooting](#troubleshooting)
- [Running Python Programs from a Terminal](#running-python-programs-from-a-terminal)

## Introduction

This chapter explains how to install Python, run code snippets in the terminal, and create your first 'Hello World!' program in Python.  

The first thing you need to do is set up your programming environment. This involves installing Python on your operating system and VSCode, a code editor, to create your algorithms.  

### Setting Up Your Programming Enviroment

In the next section, we will discuss how to install Python and VSCode on your operating system. The book version I am reading is tailored for Python 3.11 but should be compatible with Python 3.9 or later."

### Running Snippets of Python Code

You can launch Python's interpreter in a terminal window by simply typing `python` or `python3`. An example is shown below:

    python3
    >>>

The three angle brackets (`>>>`) symbol indicates that the Python Interpreter is running and is referred to as the Python prompt.

### About VS Code

As the book says:

> VS Code can be installed on all modern operating systems, and it supports most programming languages, including Python.  


## Python on Different Operating Systems

### Windows

Window's doesn't usually come with python. So you should do a cheking process to see if it is installed before trying to install.

#### Checking:

1. Open CMD (Command Prompt) app.
2. Enter `python` or `python3` in lowercase.

If you get a Python Prompt `>>>` in response, Python is installed.

#### Installing Python:

1. Visit [Python's](https://python.org) website.
2. Search for the download section.
3. Install the latest version of Python.

Be sure to select the option "Add Python to PATH" during the installation, or you will need to add it manually afterward.

### Installing VS Code

1. Visit [VS Code's](https://code.visualstudio.com) site
2. Click the Download for Windows button.
3. Run the installer.

### MacOS

MacOS's doesn't usually come with python. So you should do a cheking process to see if it is installed before trying to install.

#### Checking:  

1. Open a terminal window.
2. Type `python` or `python3` in lowercase.
3. If a prompt to install command line developer tools appears, it is better to install it later, so cancel the pop-up window.

If the output indicates you have Python 3.9 or a later version installed, you will need to install a newer version to use the code from the book.

#### Installing the Latest Version of Python:

1. Visit the [Python](https://python.org) website.
2. Navigate to the download section.
3. Click the "Download" button.
4. Run the installer.
5. A Finder window should appear.
6. Double-click the `Install Certificates.command` file.

### Installing VS Code

1. Visit the [VS Code](https://code.visualstudio.com) website.
2. Click the "Download" button.
3. Open a Finder window and navigate to the Downloads folder.
4. Drag the Visual Studio Code installer to your Applications folder and double-click the installer to run it.

### Linux

Most Linux Systems have Python alread installed.

#### Installing Python:

If Python isn't already installed, you should search online for how to install Python on your specific Linux distribution. Look for the official documentation or guidance on using your package manager to install Python.

### Installing VS Code

You should search online for how to install VS Code on your specific Linux distribution. Look for the official documentation or guidance on using your package manager to install Python.

## Running a Hello World Program


### Installing the Python Extension for VS Code 

As the books says:

> With a recent version of Python and VS Code installed, you’re almost ready
to run your first Python program written in a text editor. But before doing
so, you need to install the Python extension for VS Code.

To install extensions on VS Code, first click on the Extensions icon in the left sidebar. If you don't see the Extensions icon, go to the Manage icon (it looks like a gear in the bottom left corner) and select "Extensions." In the Extensions view, enter "Python" in the search box, locate the `Python` extension in the search results, and click "Install" to add it to your editor.

### Running hello_world.py

Create a folder wherever you want on your computer. Open VS Code and go to "File" in the top left corner, then select "Open Folder." Browse to find the folder you created and select it. Once the folder is open in VS Code, click on the "New File" icon in the left sidebar (Explorer view). Create a new `.py` file, such as `new_program.py`, by naming your file with the `.py` extension.  

After you've saved your file, enter the following line in the editor:

`print("Hello, World!")`  

To run your program, go to `Run > Run Without Debugging`. A terminal window should open at the bottom of VS Code with "Hello, World!" displayed.

## Running Python Programs from a Terminal

On your terminal you should search for your `.py` program and type.

for windows:  
`python program.py`   
MacOS or Linux:  
`python3 program.py`
