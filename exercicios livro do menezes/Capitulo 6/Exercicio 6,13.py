T = [ -10, -8, 0, 1, 2, 5, -2, -4]
maximo = T[0]
minimo = T[0]
y = 0
soma =0
for e in T:
    if e >maximo:
        maximo = e        
for x in T:
    if x < minimo:
        minimo = x
while y < len(T):
    soma += T[y]
    y += 1
    
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"A média é {(soma/len(T)):.2f}")