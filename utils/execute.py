import os
import sys

def execute(program_file, python_code):
    print("Executing: {} {}".format(program_file, python_code))
    try:
        if sys.version_info < (3,0):
            os.system("python -c '{}' {}".format(python_code, program_file))
        else:
            os.system("python -c '{}' {}".format(python_code, program_file))
    except Exception as e:
        print("Error: {}".format(e))
