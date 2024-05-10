import pathlib
from pathlib import Path

def create_project_directory(directory_name: str) -> None:
    """
    Creates a project sub directory.
    :param directory_name: Name of the directory to be created, eg "test"
    """
    pathlib.Path(directory_name).mkdir(exist_ok=True)

def create_file_or_directory(fname):
    path = Path(fname)

    if '/' in fname or '\\' in fname:
        print("Detected a slash or backslash. Please use Path.joinpath() to combine paths.")
    elif fname.endswith('.py') or fname.endswith('.md'): 
        # Create a file if it doesn't exist
        if not path.exists():
            path.touch(exist_ok=True)
            print(f"File '{fname}' created.")
        else:
            print(f"File '{fname}' already exists.")
    else:
        # Create a directory
        if not path.exists():
            path.mkdir(exist_ok=True)
            print(f"Directory '{fname}' created.")
        else:
            print(f"Directory '{fname}' already exists.")



def main():
    create_project_directory('test')
    create_project_directory('docs')
    
""" 
   # Example usage
    create_file_or_directory('test.py')        # For a Python file
    create_file_or_directory('my_directory')   # For a directory
    create_file_or_directory('example.txt')    # Neither a Python file nor a Markdown file


    # List of weekday folder names
    day_list = ["01-Mon", "02-Tue", "03-Wed", "04-Thu", "05-Fri", "06-Sat", "07-Sun"]

    # Iterate through the list and create folders
    for day in day_list:
        folder_name = f"data-{day}"
        Path(folder_name).mkdir(exist_ok=True)
        print(f"Folder '{folder_name}' created.")
    
    create_annual_data_directories(directory_name='data', start_year= 2000, end_year=2024) 

"""
if __name__ == '__main__':
    main()    
