my_list = [1, 2, 3]
for 2 in range(len(my_list)): #->>> vai criar esses valores para o for: 0,1,2
    my_list.insert(1, my_list[2])

# Passos do for:
# for 0
# [1, 1, 2, 3]
# 0  1  2  3 

# for 1
# [1, 1, 1, 2, 3]
# 0  1  2  3  4  

# for 2
# [1, 1, 1, 1, 2, 3]
# 0  1  2  3  4  5

# range(start, stop, step) se tiver somente um valor no range, é como se começasse 0 e fosse até o valor que voce solocou 
# e.g: range(6) == range(0,6) == range(0,6,1)

# len(my_list) -> retorna a quantidade de intens de dentro da lista

# append -> adiciona sempre no final da lista
# insert -> adiciona em umaposição específica