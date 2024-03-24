'''
This file contains global variables that are used in the test cases.
'''
number_of_failed_tests = 0
number_of_passed_tests = 0

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
