def do_five(f):
    f()
    f()
    f()
    f()
    f()
    
def clear_screen(f):
    do_five(f)
    do_five(f)
    do_five(f)
    do_five(f)
    do_five(f)

def print_line():
    print "-\n"
    
def foat1():
    clear_screen(print_line)
foat1()