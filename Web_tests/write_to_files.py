'''
this file is used to write the data to the output files and the console
'''
import datetime
from constants import SUCCESS_FILE_PATH, FAIL_FILE_PATH, COMBINED_FILE_PATH, LOG_FILE_PATH

def delete_file_content(file_path):
    '''
    This function deletes the content of the file
    :param file_path: the path to the file
    :return: None
    '''
    with open(file_path, 'w',encoding='utf-8') as file:
        file.write('')

def delete_all_files_content():
    '''
    This function deletes the content of all the files
    :return: None
    '''
    delete_file_content(SUCCESS_FILE_PATH)
    delete_file_content(FAIL_FILE_PATH)
    delete_file_content(COMBINED_FILE_PATH)

def write_to_file(data, file_path):
    '''
    This function writes the data to the file
    :param data: the data to write to the file
    :param file_path: the path to the file
    :return: None
    '''
    with open(file_path, 'a',encoding='utf-8') as file:
        file.write(data)
        file.write('\n')

def write_to_log_file(data : str):
    '''
    This function writes the data to the log file with its time and date 
    :param data: the data to write to the file
    :return: None
    '''
    data = f"{datetime.datetime.now()} : {data}\n"
    with open(LOG_FILE_PATH, 'a',encoding='utf-8') as file:
        file.write(data)

def write_to_combined_file(data : str):
    '''
    This function writes the data to the combined file
    :param data: the data to write to the file
    :return: None
    '''
    write_to_file(data, COMBINED_FILE_PATH)
    write_to_log_file(data)

def report_success(data : str):
    '''
    This function writes the data to the success file
    :param data: the data to write to the file
    :return: None
    '''
    write_to_file(data, SUCCESS_FILE_PATH)
    write_to_combined_file(data)
    print(data)

def report_fail(data : str):
    '''
    This function writes the data to the fail file
    :param data: the data to write to the file
    :return: None
    '''
    write_to_file(data, FAIL_FILE_PATH)
    write_to_combined_file(data)
    print(data)

def write_to_all_files(data : str):
    '''
    This function writes the data to all the files
    :param data: the data to write to the file
    :return: None
    '''
    write_to_file(data, COMBINED_FILE_PATH)
    write_to_file(data, SUCCESS_FILE_PATH)
    write_to_file(data, FAIL_FILE_PATH)
    print(data)
