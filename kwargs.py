def fmt_print(*args, **kwargs):
    separator = kwargs.get('sep', ', ')
    prefix_text = kwargs.get('prefix', '')
    string_parts = []
    for item in args:
        string_parts.append(str(item))
    combined_text = separator.join(string_parts)
    result = prefix_text + combined_text
    return result