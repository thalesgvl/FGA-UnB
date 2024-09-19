c = 0
nums = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
for n in nums:
    if n == 9:
        c += 1
print('O valor: 9 aparece: {} vezes.'.format(c))
if 3 in nums:
    print('O primeiro valor: 3 está na posição: {}.'.format(nums.index(3)+1))
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ',end='')
for n in nums:
    if n % 2 == 0:
        print(n, end=' ')
