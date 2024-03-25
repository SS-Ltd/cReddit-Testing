'''
This file contains global variables that are used in the test cases.
'''
number_of_failed_tests = 0
number_of_passed_tests = 0
first_login = True
def increment_number_of_failed_tests():
    '''
    This function increments the number of failed tests
    :return: None
    '''
    global number_of_failed_tests
    number_of_failed_tests += 1

def increment_number_of_passed_tests():
    '''
    This function increments the number of passed tests
    :return: None
    '''
    global number_of_passed_tests
    number_of_passed_tests += 1

def get_number_of_failed_tests():
    '''
    This function returns the number of failed tests
    :return: int
    '''
    return number_of_failed_tests

def get_number_of_passed_tests():
    '''
    This function returns the number of passed tests
    :return: int
    '''
    return number_of_passed_tests

def set_first_login(value: bool):
    '''
    This function sets the first login value
    :param value: The value to set
    :return: None
    '''
    global first_login
    first_login = value

def get_first_login():
    '''
    This function returns the first login value
    :return: bool
    '''
    return first_login

