string_um = "CTA"
string_dois = "ABC"
string_tres = ""

for letra in string_um:
    if letra not in string_dois and not letra in string_tres:
        string_tres += letra
        
for letra in string_dois:
    if letra not in string_um and not letra in string_tres:
        string_tres += letra

if string_tres == "":
    print("Nenhum caractere da string dois foi encontrado na string um")
print(string_tres)