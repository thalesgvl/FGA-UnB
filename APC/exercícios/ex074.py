from random import randint
nums = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ',end='')
for n in nums:
    print('{} '.format(n), end= '')
print('\nO maior valor sorteado foi: {}.'.format(max(nums)))
print('O menor valor sorteado foi: {}.'.format(min(nums)))