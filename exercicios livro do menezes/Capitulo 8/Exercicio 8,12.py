def string_lista(s, lista):
    return s in lista

L = ["AB", "CD", "EF", "FG"]

print(string_lista("AB", L))
print(string_lista("CD", L))
print(string_lista("EF", L))
print(string_lista("FG", L))
print(string_lista("XYZ", L))