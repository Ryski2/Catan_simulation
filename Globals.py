print_level = 0 #number of indents in the print statement, and also determines how much you want to print
#0 should always be printed, 1 is less necessary stuff, 2 is even less necessary, so on

def v_print(str, level):
    if level <= print_level:
        print(str)
