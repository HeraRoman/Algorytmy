def fmt_print(*args, sep=', ', prefix=''):
    texts = []
    for arg in args:
        texts.append(str(arg))
    result = '; '.join(texts)
    return prefix + result