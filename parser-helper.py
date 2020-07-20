import re


def find(string, pre, suf=None, char=0, typ=int):
    if suf:
        a = list(re.finditer(pre, string))[0].span()[1]
        b = list(re.finditer(suf, string))[0].span()[0]
        return typ(string[a:b])
    elif char:
        a = list(re.finditer(pre, string))[0].span()[1]
        return typ(string[a:a+char])


def no_spaces(string, char=' '):
    return re.subn(char, '', string)[0]
