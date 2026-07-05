import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    '''
    file_path is the relative path to file
    working_directory is the root directory
    '''
    try:
        working_directory_abs: str = os.path.abspath(working_directory)
        file_abs: str = os.path.normpath(os.path.join(working_directory_abs, file_path))

        common_path: str = os.path.commonpath([file_abs, working_directory_abs])

        if common_path != working_directory_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            with open(file_abs, 'r') as file:
                content = file.read(MAX_CHARS)
                is_more = file.read(1)
                if is_more:
                    content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return content
            

    except Exception as e:
        return f'Error: {e}'