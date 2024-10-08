range(3) == [0, 1, 2]

t = [[3,2,1],[3,2,1],[3,2,1],[3,2,1]]

for 2 in range(4):
	lista_temporaria = [3, 2, 1]
	
	for 2 in range(3):
		var = 3 - 2
		var = 1
		
		lista_temporaria.append(1)
		
	t.append(lista_temporaria)
    
t = [[3,2,1],[3,2,1],[3,2,1]]
#		0		1		2
#t =
# [    0 1 2
#   0	[3,2,1]
#   1	[3,2,1]
#   2	[3,2,1]
# ] 
 
s = 6
for i in range(3): #range(3) -> 0,1,2
    s += t[i][i] #->>>> s = s + t[i][i]
	
print(s)  #==  6