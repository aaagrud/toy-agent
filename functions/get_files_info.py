import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def file_dir_details(name: str, path: str):
    return f"{name}: file_size={os.path.getsize(path)}, is_dir={os.path.isdir(path)}"

def get_files_info(working_directory: str, directory: str = ".") -> str:
    '''
    directory is the relative path to file
    working_directory is the root directory
    '''
    try:
        working_directory_abs: str = os.path.abspath(working_directory)
        directory_abs: str = os.path.normpath(os.path.join(working_directory_abs, directory))

        common_path: str = os.path.commonpath([directory_abs, working_directory_abs])

        if common_path != working_directory_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(directory_abs):
            return f'Error: "{directory}" is not a directory'
        else:
            contents = os.listdir(directory_abs)
            data = [file_dir_details(content, os.path.normpath(os.path.join(directory_abs, content))) for content in contents]
            directory_string = ("current" if directory == '.' else directory)
            return f"Result for {directory_string} directory:\n- " + '\n- '.join(data)

    except Exception as e:
        return f'Error: {e}'





