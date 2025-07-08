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
        
        if os.path.isdir(directory) is False:
            return f'Error: "{directory}" is not a directory'
        
        directory_contents = os.listdir(directory) # Stores contents in list
        
        if len(directory_contents) != 0:
            for entry in directory_contents:
                file_name = entry
                file_size = directory + file_name
                is_dir = os.path.isdir(directory + file_name)

                print(f'- {file_name}: file_size={file_size} bytes, is_dir={is_dir}')

            

    except Exception as e:
        return f'Error: "{e}"'
    

