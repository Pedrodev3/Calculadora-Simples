# Calculadora Python

print('Calculadora Simples')
print('Operacoes Aritmeticas: (+) (-) (*) (/)')
print('Sinal para encontrar o resultado: (=)')

n = int(input('Numero: '))
op = input('Operação: ')
result = n
maior = n
menor = n

while op != '=':
    n = int(input('Número: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
        
    if op == '+':
        result += n
    elif op == '-':
        result -= n
    elif op == '*':
        result *= n
    elif op == '/':
        result /= n
    print(f'Resultado: {result}')
    
    # Result
    op = input('Operação: ')          
print(f'Valor final: {result}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')