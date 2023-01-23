lista = ["Eli", "Mary"]


#print ("\n".join(lista))

print ([x for x in lista if x.lower() == "mary"])

for x in lista[::-1]:
    print (x)