a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)


nome = "Luiz"
idade = 23
formato1 = f'{nome} tem {idade:.2f} anos'
print(formato1)