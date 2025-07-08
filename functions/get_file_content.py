import os

def get_file_content(working_directory, file_path):
    supplied_file_path = file_path

    try:
        if file_path is not None:
            file_path = os.path.join(working_directory,file_path)
        
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(file_path)

        if not abs_file_path.startswith(abs_working_dir): # Check if absolute file path is prepended with working dir
            return f'Error: Cannot read "{supplied_file_path}" as it is outside the permitted working directory'
        
        is_file = os.path.isfile(file_path)
        if is_file == False:
            #print(os.path.join(working_directory,file_path))
            #print(full_file_path)
            return f'Error: File not found or is not a regular file: "{supplied_file_path}"'

        with open(file_path, "r") as file:
            read_file = file.readlines()
            return "".join(read_file)
        
        read_file.close()
        
    except Exception as e:
        return f"Error: {e}"