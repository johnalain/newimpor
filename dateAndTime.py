from datetime import datetime

now: datetime = datetime.now()#output 12.03.24
print(f'{now:%d.%m.%y (%H:%M:%S)}')#output 12.03.24 (10:27:07)
print(f'{now:%c}')#Tue Mar 12 10:29:31 2024
print(f'{now:%I%p}')#10AM

# U CAN SEARCH GOOGLE FOR DATE TIME 
n:float = 1234.5678
print(n)
print(round(n, 2))#output 1234.57
print(f'{n:.3f}')#output 1234.568
print(f'Result:{n:.4f}')#Result:1234.5678
print(f'Result:{n:.0f}')#Result:1235
print(f'Result:{n:,.2f}')#Result:1,234.57
print('@'*20)
a: int = 10
b: int = 5
print(f'a+b = {a+b}')#a+b = 15
my_var = 'mike says hi'
#https://youtu.be/EoNOWVYKyo0?t=490
print(f'{a+b = }')#a+b = 15
print('@'*20)
print(f'{bool(a) = }')#bool(a) = True
print(f'{my_var = }')#my_var = 'mike says hi'


