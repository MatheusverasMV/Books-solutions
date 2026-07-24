primeira = "AATTGGAA"
segunda = "TG"
terceira = ""

for i in primeira:
    if i not in segunda:
        terceira += i

if terceira == "":
    print("Nenhum caractere da string dois foi encontrado na string um")
    
print(terceira)