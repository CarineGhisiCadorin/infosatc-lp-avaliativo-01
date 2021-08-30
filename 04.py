a1 = float(input("Informe o valor do premio: "))
a2 = a1 * 0.07
c = 0.46 * a1 - a2
d = 0.32 * a1 - a2 
e =   a1 - (c+d) - a2
print("O valor do primeiro ganhador é:" ,c,"R$")
print("O valor do segundo  ganhador é:" ,d,"R$")
print("O valor do terceiro ganhador é:" ,e,"R$")
print("O valor do imposto é:" ,a2,"R$")


