import utils.injection as inject
import utils.executable_checking as checker

if __name__ == "__main__":
    program_file = input("[*] Enter the program file: ")
    if checker.is_running(program_file):
        print("[*] Entering to the executable...")
        inject.inject_to_running(program_file)
        print("[*] Entered!")
    else:
        print("[*] Opening...")
        inject.inject_to_starting(program_file)
        print("[*] Opened!")