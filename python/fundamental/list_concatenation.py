catnmaes =[]

while True:
    print('Enter the name of cat ' + str(len(catnmaes) + 1) + '(Or enter nothing to stop.):')
    name = input()

    if name == '':
        break
    catnmaes = catnmaes +[name]
print('The cat names are:')
for name in catnmaes:
    print(' '+ name)