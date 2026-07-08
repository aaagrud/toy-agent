import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a python file relative to the working directory, returns the output.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "file path to file to run, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "description": "optional arguments for the file that is to be executed",
                    "items": {
                        "type": "string"
                    }
                },
            },
        },
    },
}

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_directory_abs: str = os.path.abspath(working_directory)
        file_abs: str = os.path.normpath(os.path.join(working_directory_abs, file_path))

        common_path: str = os.path.commonpath([file_abs, working_directory_abs])

        if common_path != working_directory_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'       
        if not os.path.isfile(file_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if file_path.split('.')[-1] != 'py':
            return f'Error: "{file_path}" is not a Python file'
        else:
            command = ["python3", file_abs]
            if args:
                command.extend(args)
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
            output = ''
            if result.returncode != 0:
                output += f"Process exited with code {result.returncode}"
            if not result.stdout and not result.stderr:
                output += "\nNo output produced"
            else:
                output += f"\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"
            return output
    except Exception as e:
        return f"Error: executing Python file: {e}"