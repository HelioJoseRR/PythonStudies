from employee import Employee
import pytest

@pytest.fixture
def employee():
    return Employee('helio', 'jose', 5000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.anual_salary == 10000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.anual_salary == 15000