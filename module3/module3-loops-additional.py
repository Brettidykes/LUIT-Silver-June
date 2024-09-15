#remember the else branch of a loop is always executed exactly once (exception: break statement)

for a in range(1,6):
    for b in range (1, 6):
        print(a, 'x', b, '=', a * b)