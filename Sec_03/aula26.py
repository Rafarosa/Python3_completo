"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABc'
print(f'{variavel}')
print(f'{variavel:0>10}')
print(f'{variavel:0<10}')
print(f'{variavel:0^10}')
print(f'{-1000.456789567544:0=+10,.2f}')
print(f'o hexadeciamal de 1500 é {1500:08x}')
print(f'{variavel!r}')