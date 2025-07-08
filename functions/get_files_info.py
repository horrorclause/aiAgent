import os

def get_files_info(working_directory, directory=None):

    supplied_directory = directory # User submitted directory
    
    try:
        if directory is not None:
            directory = os.path.join(working_directory, directory)
        
        else:
            directory = working_directory

        ap_working_dir = os.path.abspath(working_directory) # Absolute path of working directory
        ap_directory = os.path.abspath(directory) # Absolute Path of directory

        if not ap_directory.startswith(ap_working_dir):
            return f'Error: Cannot list "{supplied_directory}" as it is outside the permitted working directory'
            

    except Exception as e:
        return f'Something happened: {e}'
    