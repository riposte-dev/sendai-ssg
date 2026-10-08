import os
import time
from modules import config

PATH_INPUT = config.get_config("PATH_INPUT") # Directory for all source files in markdown
DATE_FORMAT = config.get_config("DATE_FORMAT") # Default format for get_file_creation_date() and get_file_modified_date()

def get_file_creation_date(file):
    created_seconds = os.path.getctime(PATH_INPUT + file)
    created_formatted = time.ctime(created_seconds)

    time_object = time.strptime(created_formatted)
    date = time.strftime(DATE_FORMAT, time_object)

    return date


def get_file_modified_date(file):
    modified_seconds = os.path.getmtime(PATH_INPUT + file)
    modified_formatted = time.ctime(modified_seconds)
    
    time_object = time.strptime(modified_formatted)
    date = time.strftime(DATE_FORMAT, time_object)

    return date

