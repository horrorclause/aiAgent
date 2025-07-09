import os

def write_file(working_directory,file_path,content):
    
    supplied_file_path = file_path

    try:
        os.makedirs(working_directory, exist_ok=True)
        
        if file_path is not None:
            file_path = os.path.join(working_directory,file_path)        

        # Checks if file exists, if not it creates it
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("")
            print(f'Created file: {file_path}')
            f.close()
        else:
            print(f'File already exists: {file_path}')
            

        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(file_path)

        # Checks if the supplied file path is contained within the working directory
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot write to "{supplied_file_path}" as it is outside the permitted working directory'
        
        # Checks if file is actually a file or something else
        is_file = os.path.isfile(file_path)
        if is_file == False:
            return f'Error: File not found or is not a regular file: "{supplied_file_path}"'
        
        with open(file_path, "w") as file:
            file.write(content)
            file.close()
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        print(f'Error: {e}')
