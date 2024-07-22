numberlist = list()
while True:
    value = input()
    if value == 'done': break
    out = float(value)
    numberlist.append(out)
average = sum(numberlist)/len(numberlist)
print('El promedio es:', average)
