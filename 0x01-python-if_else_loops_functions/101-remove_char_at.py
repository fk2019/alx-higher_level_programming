def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return str
    i = 0
    start = ""
    end = ""
    while (i < n):
        start = start + str[i]
        i += 1
    i = n + 1
    while (i < len(str)):
        end = end + str[i]
        i += 1
    return (start + end)
