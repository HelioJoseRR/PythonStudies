# Testing Your Code

This is the appendix for this chapter:

1. [Introduction](#introduction)
2. [Installing pytest with pip](#installing-pytest-with-pip)
3. [Testing a Function](#testing-a-function)
4. [Testing a Class](#testing-a-class)
5. [Using Fixtures](#using-fixtures)  

You can also find the codes from this section in the [codes](./codes) directory.  

[RETURN](./../../README.md)  

## Introduction  

In this chapter, you will learn to test your code using `pytest`.  

## Installing pytest with pip  

You shouldn’t blindly trust every third-party package, but you also shouldn’t be put off by the fact that a lot of important functionality is implemented through such packages.  

### Updating pip  

pip is used to install third-party packages.  

Open a new terminal window and issue the following command:  

```
python -m pip install --upgrade pip
```  

The first part of this command, python -m pip, tells Python to run the module pip. The second part, install --upgrade, tells pip to update a package that’s already been installed.  

### Installing pytest  

```
python -m pip install --user pytest
```
> If you have any difficulty running this command, try running the same command without the --user flag.  

The `--user` tag tells pip to install the package only in the current user.  

## Testing a Function  

We'll use this function named `name_function.py` to learn about testing:  

```python
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()
```  

Then we'll create a program named `name.py` that asks the user his name:  

```python
from name_function import get_formatted_name


print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
```  

### Unit Tests and Test Cases  

A unit test verifies that one specific aspect of a function’s behavior is correct.  

A test case is a collection of unit tests that together prove that a function behaves as it's supposed to.  

### A Passing Test  

We'll write a single test function:  

```python
from name_function import get_formatted_name


def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""  

    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
```  

The name of a test must start with `test_` because pytest will search for it.  

Also, test names should be longer and more descriptive than a typical function name.  

An assertion is a claim about a condition. Here we’re claiming that the value of formatted_name should be 'Janis Joplin'.  

### Running a Test  

If you run the file `test_name_function.py` directly, you won’t get any output because we never called the test function.  

To do this, open a terminal window and navigate to the folder that contains the test file.  

```
pytest
```  

>[TRY IT YOURSELF 11.1 - 11.2](./codes/)   

## Testing a Class  

### A Variety of Assertions  

So far, you’ve seen just one kind of assertion: a claim that a string has a specific value.  

Anything that can be expressed as a conditional statement can be included in a test.  

| Assertion | Claim |
| --- | --- |
| assert a == b | Assert that two values are equal. |
| assert a != b | Assert that two values are not equal. |
| assert a | Assert that a evaluates to True. |
| assert not a | Assert that a evaluates to False. |
| assert element in list | Assert that an element is in a list. |
| assert element not in list | Assert that an element is not in a list. |  

### A Class to Test  

Testing a class is similar to testing a function, because much of the work involves testing the behavior of the methods in the class.  

Let's use this class named `survey.py` as an example:  

```python
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Show the survey question."""
        print(self.question)
    
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
    
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
```  

Let's use this program named `language_survey.py`:

```python
from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)
#
#  Show the question, and store responses to the question.
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
    break
    language_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()
```  
### Testing the AnonymousSurvey Class  

Let's write a test named `test_survey.py` that verifies one aspect of the way AnonymousSurvey behaves.  

```python
from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
```  

If we wanna test more than 1 response to the survey:  

```python
from survey import AnonymousSurvey

def test_store_single_response():
    --snip--

def test_store_three_responses():
    """Test that three individual responses are stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    
    for response in responses:
        assert response in language_survey.responses
```  

### Using Fixtures  

In testing, a fixture helps set up a test environment. Often, this means creating a resource that’s used by more than one test. We create a fixture in pytest by writing a function with the decorator `@pytest.fixture`.  

A decorator is a directive placed just before a function definition; Python applies this directive to the function before it runs, to alter how the function code behaves.  

```python
import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    
    for response in responses:
        assert response in language_survey.responses
```  

>[TRY IT YOURSELF 11.3](./codes/)  

