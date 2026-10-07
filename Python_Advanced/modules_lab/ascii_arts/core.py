from pyfiglet import figlet_format

def print_text(some_text:str) -> str:
    return figlet_format(some_text)