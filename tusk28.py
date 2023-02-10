def rec_sum(a, b):
    if  b == 0:
        return a
    return rec_sum(a+1, b-1)        
a = int(input('введите число 1 А: '))
b = int(input('введите число 2 B: ')) 
print('сумма двух чисел ', a, '+', b, ' равна: ', rec_sum(a, b))