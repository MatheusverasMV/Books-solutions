preço = float(input("Diga o preço da mercadoria: "))
desconto = float(input("Diga o porcentual de desconto: "))
print("O desconto é de %5.2f"%(preço*desconto/100))
print("O valor final do produto é R$ %5.2f"%(preço+preço*desconto/100))