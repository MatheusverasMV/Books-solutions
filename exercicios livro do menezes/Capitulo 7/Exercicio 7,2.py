string_um = "AAACTBF"
string_dois = "CTB"
string_tres = []

for i in string_um:
    if i in string_dois:
        string_tres.append(i)
        
if string_tres == []:
    print("Nenhum caractere da string dois foi encontrado na string um")
print("".join(string_tres))