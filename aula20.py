#a = 4
#b = 5
#s = a + b
#print(s)
#a = 8
#b = 9
#s = a + b
#print(s)
#a = 2
#b = 1
#s = a + b
#print(s)
#pra não virar uma rotina:
#def soma(a, b):
#    print(f'A = {a} e B = {b}')
#    s = a + b
#    print(s)
#    print(f'A soma A + B = {s}')



#soma(4, 5)
#soma(8, 9)
#soma(2, 1)
#soma(b=4, a=5)
#soma(7, 2)
#soma(3, 9, 5)


#def contador(* núm):
#    for valor in núm:
#        print(valor, end='')
#    print('FIM')

#contador(2, 1, 7)
#contador(8, 8)
#contador(4, 4, 7, 6, 2)

#def contador(* núm):
#    tam = len(núm)
#    print(f'Recebi os valores {núm} e são ao todo {tam} números')

#contador(2, 1, 7)
#contador(8, 8)
#contador(4, 4, 7, 6, 2)

#def dobra(lst):
#    pos = 0
#    while pos < len(lst):
#        lst[pos] *= 2
#        pos += 1

#valores = [6, 3, 9, 1, 0, 2]
#dobra(valores)
#print(valores)

def soma(* valores):
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)
