x = int(input('please enter first number:',  ))
y = int(input('please enter second number:',  ))
z = str(input('please enter the required operation from the following (sum, minus, mult, div):',))
if z == 'sum':
  print(x + y)
elif z == 'minus':
  print(x-y)
elif z == 'mult':
  print(x*y)
elif z == 'div':
  print(x/y)
else:
  print('unknown operation')