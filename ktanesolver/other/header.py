import os

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def header():
    clear_screen()
    print("="*30)
    print("KTaNE Solver - Python".center(30))
    print("="*30)