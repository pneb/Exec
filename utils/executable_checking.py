import psutil

def is_running(process_name):
    for process in psutil.process_iter():
        try:
            if process.name() == process_name:
                return True
        except:
            pass
    return False
