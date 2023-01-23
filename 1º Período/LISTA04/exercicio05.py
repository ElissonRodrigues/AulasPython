from re import search 

def validar_ip(IP):
    return search("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$", IP)

IP = input("Qual o endereço IP: ") 

if validar_ip(IP):
	print (f"\nEndereço IP: {IP} -  ✅ VÁLIDO")
else:
	print (f"\nEndereço IP: {IP} -  ❌ INVÁLIDO")