import struct

formato_req = '!i 20s i'
tamanho_req = struct.calcsize(formato_req)

pacote = struct.pack(formato_req, 1, 'teste'.encode(), 1)

inteiro1, string, inteiro2 = struct.unpack(formato_req, pacote)

print (pacote)
print (inteiro1)
print (inteiro2)
print (string.decode())
'''
formato_resp = '!i 20s'

pacote_resp = struct.calcsize(formato_resp)


'''