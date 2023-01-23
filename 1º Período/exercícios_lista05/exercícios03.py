def fibonacci(n):
	e1 = 0
	e2 = 1
	
	print ("\n\nRESULTADOS DO EXERCÍCIO 4")
	print ("="*50)
	print (f"| {e1} | {e2} | ", end="")
	
	for x in range(n-2):
	    e3 = e1 + e2
	    e1 = e2
	    e2 = e3
	
	    print (f"{e3} | ", end="")
	 
	print ("")
	print ("="*50)
	
n = int(input("Quantas numeros da equência de você deseja?: "))
fibonacci(n)
