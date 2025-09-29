def fmt_print(*args, **kwargs):
    sep = kwargs.get('sep', ', ')
    prefix = kwargs.get('prefix', '')
    args_as_strings = [str(arg) for arg in args]
    result = sep.join(args_as_strings)
    if prefix:
        result = prefix + result
    return result
print(fmt_print(1, 2, 3, sep='; ', prefix='nums: '))
print(fmt_print('x'))
print(fmt_print('a', 'b', 'c'))
print(fmt_print(10, 20, prefix='Numbers: '))