invited_guests = ['Kate', 'adam', 'jon', 'harry']
name = input('what is your name? ')
if name in invited_guests:
    print('Welcome')
else:
    print('You are not invited!')

invited_guests = ['Kate', 'adam', 'jon', 'harry']
name = input('what is your name? ')
if name not in invited_guests:
    print('You are not invited!')
else:
    print('Welcome!')