import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    '''
    file_path is the relative path to file
    working_directory is the root directory
    content is the content u wanna write to file_path
    '''
    try:
        working_directory_abs: str = os.path.abspath(working_directory)
        file_abs: str = os.path.normpath(os.path.join(working_directory_abs, file_path))

        common_path: str = os.path.commonpath([file_abs, working_directory_abs])

        if common_path != working_directory_abs:
            return f'Error: Cannot write to "{file_abs}" as it is outside the permitted working directory'
        if os.path.isdir(file_abs):
            return f'Error: Cannot write to "{file_abs}" as it is a directory'
        else:
            os.makedirs(os.path.dirname(file_abs), exist_ok=True)
            with open(file_abs, 'w') as file:
                file.write(content)
            return f'Successfully wrote to "{file_abs}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'