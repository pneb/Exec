import os
import utils.execute as execute

def inject_to_running(program_file):
    program_file = os.path.abspath(program_file)
    python_code = input("[*] Enter the code [use \\n for longer codes]: ")
    execute.execute(program_file, python_code)

def inject_to_starting(program_file):
    python_code = input("[*] Enter the code [use \\n for longer codes]: ")
    execute.execute(program_file, python_code)