from random import randint


def progress(a, b, c):
    i = 0
    prog = []
    while i < c:
        prog.append(a)
        i += 1
        a = a + b
    return prog

first_number = randint(1, 10)
step = randint(1, 10)
prog_len = randint(5, 10)
prog = progress(first_number, step, prog_len)

print(prog)


rand_num = randint(0, prog_len - 1)
result = str(prog[rand_num])
prog[rand_num] = '..'

print(prog)

prog_str = ' '.join(str(el) for el in prog)

print(prog_str)
print(result)