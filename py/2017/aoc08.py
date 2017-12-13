import re
def check_var(varname):
    try:
        exec(varname)
    except NameError:
        exec('globals()[varname] = 0')
def is_digit(x):
    try:
        int(x)
        return True
    except (ValueError, TypeError) as e:
        return False

def globals_max():
    digits = [d for d in globals().values() if is_digit(d)]
    return max(digits)
def process_input(filename):
    with open(filename) as file:
        regex = re.compile(r'^(\w+)\s+(inc|dec)\s+(-*\d+)\s+if\s+((\w+).*$)')
        for l in file:
            (var_op, op, val_op, condition, var_con) = regex.search(l).groups()
            check_var(var_op)
            check_var(var_con)
            if eval(condition):
                op_str = '+=' if op == 'inc' else '-='
                exec('global {0};{0} {1} {2}'.format(var_op, op_str, val_op))

if __name__ == '__main__':
    process_input("input08.txt")
    print('Result = {0}'.format(globals_max()))