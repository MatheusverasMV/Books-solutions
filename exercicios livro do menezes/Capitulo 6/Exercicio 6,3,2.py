Lista1 = [4,3,5,2]
Lista2 = [4,9,8,2]
Lista_resultado = []

x = 0

while x < len(Lista1):
    if Lista1[x] not in Lista_resultado:
        Lista_resultado.append(Lista1[x])
    x += 1

x = 0

while x < len(Lista2):
    if Lista2[x] not in Lista_resultado:
        Lista_resultado.append(Lista2[x])
    x += 1

print("A lista resultado é %s" % Lista_resultado)