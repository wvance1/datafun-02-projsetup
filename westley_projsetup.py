''' 
This module provides functions for creating a series of project folders.

Current options are creating folders for a specified range, creating folders from a list,
creating folders from a list and appending a prefix, and creating folders for a specified 
period of time on an interval. 

'''

# imports
import math
import time
import pathlib
import westleyVance_utils
from datetime import datetime
import wvance_projsetup as fun


#Define reusable functions to create a series of project folders.

def create_folders_for_range(directory_name: str, start: int, end: int):
    """Creates a directory and folders for each year specified within a given range"""
    # calls function from utils to create new directory
    fun.create_project_directory(directory_name) 
    # runs for loop creating new file within the directory for each year in range
    for year in range (start, (end + 1)):
        year_directory = pathlib.Path(directory_name).joinpath(str(year))
        fun.create_project_directory(year_directory)
        print(f"Created {year_directory}")


def create_folders_from_list(input_list: list):
    """Creates folders from a provided list of names"""
    # converts list to lowercase and replaces spaces with no space
    input_list = [name.lower() for name in input_list]
    input_list = [name.replace(" ", "") for name in input_list]
    #runs for loop creating folder for each element in list
    for val in input_list:
        pathlib.Path(val).mkdir(exist_ok=True)
        print(f"Folder '{val}' created.")


def create_prefixed_folders(folder_list: list, prefix: str):
    """Creates folders from a given list of names and appends a provided prefix to the front of each lost element"""
    # converts list to lowercase and replaces spaces with no space
    folder_list = [name.lower() for name in folder_list]
    folder_list = [name.replace(" ", "") for name in folder_list]
    #runs for loop creating folder for each element in list and appends prefix to front of list elements
    for val in folder_list:
        folder_name = f"{prefix}{val}"
        pathlib.Path(folder_name).mkdir(exist_ok=True)
        print(f"Folder '{folder_name}' created.")

def create_folders_periodically(duration: int, total_time: int):
    """Creates folders every 'duration' in seconds for a specified 'total_time' in seconds."""
    # takes total time and divides by duration to find necessary number of iterations
    iterations: int = math.floor(total_time / duration)
    #iterates a specified number of times, creating a new folder every 'duration' seconds.
    #folder named based on time.
    x: int = 0
    while x < iterations:
        val: str = datetime.now().strftime('%Y-%m-%d_%H%M%S')
        pathlib.Path(val).mkdir(exist_ok=True)
        print(f"Folder '{val}' created.")
        x += 1
        if x < iterations:
            time.sleep(duration)



def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    boo: bool = True
    while boo:
        try:
            byline_yn: str = input(f"would you like to hear the byline from the knockoff fast food firm? ")
            if byline_yn.lower() == "yes" or byline_yn.lower() == "y":
                print(f"Byline: {westleyVance_utils.byline()}")
            boo = False    
        except:
            print(f"Oops! you did something goofy. Try again!")
            boo = True
   
    boo = True
    while boo:
        try:   
            # Call function 1 to create folders for a range (e.g. years)
            year_yn: str = input(f"would you like to create a folder for a specified year rage? ")
            if year_yn.lower() == "yes" or year_yn.lower() == "y":
                folder_name: str = input(f"enter a folder name for the desired year range: ")
                start_year: int = int(input(f"enter a starting year: "))
                end_year: int = int(input(f"enter an end year: "))
                create_folders_for_range(folder_name,start_year, end_year)
            boo = False    
        except:
            print(f"Oops! you did something goofy. Try again!")
            boo = True

    boo = True
    while boo:
        try:  
            # Call function 2 to create folders given a list
            list_yn: str = input("Would you like to create a folder for each item in the provided list? ")
            if list_yn.lower() == "yes" or list_yn.lower() == "y":
                folder_names: list = ['data-csv', 'data-excel', 'Data-json']
                create_folders_from_list(folder_names)
            boo = False    
        except:
            print(f"Oops! you did something goofy. Try again!")
            boo = True
    
    boo = True
    while boo:
        try: 
            # Call function 3 to create folders using comprehension
            prefix_yn: str = input(f"Would you like to append a prefix 'data-' to the provided list? ")
            if prefix_yn.lower() == "yes" or prefix_yn.lower() == "y":
                folder_names: list = ['csv', 'excel', 'json']
                prefix: str = 'data-'
                create_prefixed_folders(folder_names, prefix)
            boo = False    
        except:
            print(f"Oops! you did something goofy. Try again!")
            boo = True

    boo = True
    while boo:
        try: 
            # Call function 4 to create folders periodically using while
            timer_yn: str = input(f"Would you like to create folders for a specified time interval? ")
            if timer_yn.lower() == "yes" or timer_yn.lower() == "y":
                duration_secs: int = 5  # duration in seconds
                total_time: int = int(input("how long would you like to run this file creator for in seconds: "))
                create_folders_periodically(duration_secs, total_time)
            boo = False    
        except:
            print(f"Oops! you did something goofy. Try again!")
            boo = True


if __name__ == '__main__':
    main()
