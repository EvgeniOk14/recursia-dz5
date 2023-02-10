def degree(a,b):
    if b == 1:
        return a 
    if b !=1:
        return (a * degree(a, b-1))    
a = int(input('введите число А: '))
b = int(input('введите степень B: '))    
print(a, 'в степени ', b, ' равно: ', degree(a,b))

