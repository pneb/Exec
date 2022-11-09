import psutil

def is_running(program_file):
    program_file = program_file.replace("\\", "/")
    for process in psutil.process_iter():
        try:
            filename = process.exe().replace("\\", "/")
            if filename == program_file:
                return True
        except:
            pass
    return False