#task 1
# a = input('Please enter an offer: ')
# s = a.count(' e')
# print(s)


#task 2
# a = input('Please enter an offer: ')
# s = a.replace(':', '%')
# print(s)


#task 3
# a = input('Please enter an offer: ')
# k = a.replace('.', '')
# s = a.count('.')
# print(k)
# print(s)


#task 4
# a = input('Please enter an offer: ')
# k = a.replace('a', 'o')
# s = a.count('a')
# print(k)
# print(s)
# print(len(a))


#task 5
# a = input('Please enter an offer: ')
# print(a.lower())


#task 6
# a = input('Please enter an offer: ')
# k = a.replace('a', '')
# s = a.count('a')
# print(k)
# print(s)


#task 7
# a = input('Please enter an offer: ')
# s = a[0: int(len(a)/2)]
# k = s.replace('p', '*')
# print(k + a[int(len(a)/2): len(a)])


#task 8
# a = input('Please enter an offer: ')
# k = a.count(' ')
# print(k + 1)


#task 9
# a = input('Please enter an offer: ')
# b = input('Please enter right word: ')
# k = a.count(b)
# print(k)


#task 10
# a = input('Please enter an offer: ')
# print(a.title())


#task 11


#task 12
# a = input('Please enter an offer: ')
# print(a.count('a '))


#task 13
# a = input('Please enter an offer: ')
# b = (a.find('(')) + 1
# c = a.find(')')
# k = a[b: c]
# print(k)


#task 14
# a = input('Please enter an offer: ')
# for i in a.split():
#     if a.startswith('a') and a.endswith('d'):
#         print(a)


#task 15
# a = input('Please enter an offer: ')
# print(a.count('t'))


#task 16
# a = input('Please enter an offer: ')
# a = a[0: a.find(' ')]
# print(a[::-1])


#task 17
# a = input('Please enter an offer: ')
# a = a[(a.rindex(' ')+1): len(a)]
# print(a)


#task 18
# a = input('Please enter a first offer: ')
# b = input('Please enter a second offer: ')
# if len(a) > len(b):
#     print(a + ' ' + b)
# else:
#     print(b + ' ' + a)


#task 19
# a = input('Please enter a first offer: ')
# b = input('Please enter a second offer: ')
# if len(a) > len(b):
#     print(a + ' ' + b)
# else:
#     print(b + ' ' + a)


#task 20/1
# a = input('Please enter an offer: ')
# f = a[0: a.find(' ')]
# l = a[a.rindex(' '): len(a)]
# print(f + l)

#task 20/2
# a = input('Please enter an offer: ')
# for i in a.split():
#     print(a[0])
#     n = a.find(' ')
#     a = a[n+1: len(a)]


#task 21
# a = input('Please enter an offer: ')
# for i in a.split():
#     n = a.find('S')
#     a = a[n+1: len(a)]
#     print(n)


#task 22
# a = input('Please enter an offer: ')
# a = a[(a.rindex(' ')+1): len(a)]
# print(a[::-1])


#task 23
# a = input('Please enter an offer: ')
# a = a[0: a.find(' ')]
# print(a[::-1])


#task 24
# a = input('Please enter an offer: ')
# print(a.replace(' ', ''))


#task 25
# a = input('Please enter an offer: ')
# for i in range(2):
#     n = a.find(' ')
#     print(a[:n])
#     a = a[n+1:]


#task 26
# a = input('Please enter an offer: ')
# if a.find('+') or a.find('-') or a.find('/') or a.find('*'):
#     print(a[a.find('+')] + a[a.find('-')] + a[a.find('/')] + a[a.find('*')])


#task 27
# a = input('Please enter an offer: ')
# for i in a.split():
#     n = a.find(' ')
#     if len(a[:n]) > 6:
#         print(a[:n])
#     a = a[n+1:]


#task 28
# a = input('Please enter an offer: ')
# for i in range(1):
#     print(a.find(' '))
#     n = a.find(' ')
#     a = a[n+1:]
# print(a.find(' ') + n)


#task 29
# a = input('Please enter an offer: ')
# for i in a.split():
#     n = a.find(' ')
#     print(a[n-1:n])
#     a = a[n+1:]


#task 30
# a = input('Please enter an offer: ')
# n = a.find(' ')
# a = a[ :n]
# print(a.upper())